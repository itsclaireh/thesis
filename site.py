#run this file to test the UI

#imports
from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn import preprocessing
from compare import compare_and_load_datasets, load_file
from clean import clean_tweet, stemmy;
from svm import svm_results,svm_results_reduction;
from naivebayes import nb_results;
from sklearn.calibration import CalibratedClassifierCV
import sys;
app = Flask(__name__)

#load data, take the agreement of male and female responses
file1 = 'data/MeTooMen.csv';
file2 = 'data/MeTooWomen.csv';
d = compare_and_load_datasets(file1, file2);

#load extra data
supp = load_file('data/supplemental.csv');
df=pd.concat([d,supp]);

#load extra data set 2
supp2 = load_file('data/suppTweetsNoID.csv');
df=pd.concat([df,supp2]);

#clean tweets
for i, row in df.iterrows():
    if row.text:
      df.at[i,'text']=clean_tweet(row.text);

#print stats to console
print('\n\n\t\t*******SVM*******');
dfrel= df.drop(df.query('related in ["1"]').sample(frac=.55,random_state=1).index);
print('\t\tRelated:\t{0}'.format(len(dfrel.loc[dfrel.related=='1'])),file=sys.stdout);
print('\t\tNot Related:\t{0}'.format(len(dfrel.loc[dfrel.related=='2'])),file=sys.stdout);
dfstance= df.drop(df.query('stance in ["1"]').sample(frac=.2,random_state=2).index);
print('\t\tSupport:\t{0}'.format(len(dfstance.loc[dfstance.stance=='1'])),file=sys.stdout);
print('\t\tAgainst:\t{0}'.format(len(dfstance.loc[dfstance.stance=='2'])),file=sys.stdout);
print('\t\tNeutral:\t{0}'.format(len(dfstance.loc[dfstance.stance=='3'])),file=sys.stdout);
dfcat= df.drop(df.query('category in ["4"]').sample(frac=0.0,random_state=3).index);
print('\t\tPatronizing:\t{0}'.format(len(dfcat.loc[dfcat.category=='1'])),file=sys.stdout);
print('Unwanted Sexual Attention:\t{0}'.format(len(dfcat.loc[dfcat.category=='2'])),file=sys.stdout);
print('\t\tPredatory:\t{0}'.format(len(dfcat.loc[dfcat.category=='3'])),file=sys.stdout);
print('\tNot Enough Context:\t{0}'.format(len(dfcat.loc[dfcat.category=='4'])),file=sys.stdout);

#from the data, select the columns we need for each classifier
dfrel=dfrel[['id_str', 'text', 'related']];
dfstance=dfstance[['id_str', 'text', 'stance']];
dfcat=dfcat[['id_str', 'text', 'category']];

#drop the NaN categories from each class
#Note: we must do it this way instead of dropping before this stage,
#since some tweet samples might only have the stance category (for example), and in those
#cases we want to drop relevant and sexual harassment category
dfrel=dfrel.dropna();
dfstance = dfstance.dropna();
dfcat=dfcat.dropna();

#each classifier for relevance, stance, and  category need their own countVect
count_vect=CountVectorizer(strip_accents='unicode');
count_vect2=CountVectorizer(strip_accents='unicode');
count_vect3=CountVectorizer(strip_accents='unicode');

#print total samples/features
print('\n\t\tRELATED:');
Xr = count_vect.fit_transform(dfrel.text);
Yr = dfrel[['related']];
Yr=np.ravel(Yr);
print('\t\tTotal Samples:\t{0}'.format(len(Yr)));
print('\t\tFeatures:\t{0}'.format(len(count_vect.get_feature_names())));

print('\n\t\tSTANCE:');
Xs = count_vect2.fit_transform(dfstance.text);
Ys = dfstance[['stance']];
Ys=np.ravel(Ys);
print('\t\tTotal Samples:\t{0}'.format(len(Ys)));
print('\t\tFeatures:\t{0}'.format(len(count_vect2.get_feature_names())));

print('\n\t\tCATEGORY:');
Xc = count_vect3.fit_transform(dfcat.text);
Yc = dfcat[['category']];
Yc=np.ravel(Yc);
print('\t\tTotal Samples:\t{0}'.format(len(Yc)));
print('\t\tFeatures:\t{0}'.format(len(count_vect3.get_feature_names())));

#TFIDF
tfidf_transformer = TfidfTransformer();
X_train_tfidf = tfidf_transformer.fit_transform(Xr)
tfidf_transformer2 = TfidfTransformer();
X_train_tfidf2 = tfidf_transformer.fit_transform(Xs)
tfidf_transformer3 = TfidfTransformer();
X_train_tfidf3 = tfidf_transformer.fit_transform(Xc)

#fit each classifier to its training data
linclf1=LinearSVC(random_state=0, C=1,loss="hinge");
clf1 = CalibratedClassifierCV(linclf1);
clf1.fit(X_train_tfidf,Yr);

linclf2=LinearSVC(random_state=0, C=1,loss="hinge");
clf2 = CalibratedClassifierCV(linclf2);
clf2.fit(X_train_tfidf2,Ys);

linclf3=LinearSVC(random_state=0, C=10,loss="hinge");
clf3 = CalibratedClassifierCV(linclf3);
clf3.fit(X_train_tfidf3,Yc);

#the dataframes to hold the user's input
#has to be in the same format as the training data
ix=range(3,1);
col=['id','text','related'];
xtestr = pd.DataFrame(index=ix,columns=col);
col=['id','text','stance'];
xtests = pd.DataFrame(index=ix,columns=col);
col=['id','text','category'];
xtestc = pd.DataFrame(index=ix,columns=col);
xtestr.at[0,'id']='1';
xtestr.at[0,'related'] = '';
xtests.at[0,'id']='1';
xtests.at[0,'stance'] = '';
xtestc.at[0,'id']='1';
xtestc.at[0,'category'] = '';


@app.route('/main',methods=['GET','POST'])

def form_example():
    #empty variables to load on the page originally
    originalTweet='';
    tweet='';
    rel='';
    stance='';
    cat='';
    probrel='';
    probstance='';
    probcat='';

    #for calculations
    rel_prob=stance_prob=cat_prob=0;

    if request.method == 'POST':
        tweet = request.form.get('tweet');

        #only evaluate the tweet if it's below the character limit
        if len(tweet) < 281:
            #keep the user's original tweet to output to them
            originalTweet=tweet;
            #perform the same clean on the user's tweet
            tweet = clean_tweet(tweet);

            #predict relevance
            xtestr.at[0,'text'] = tweet;
            x_scaled = count_vect.transform(xtestr.text);
            result1 = clf1.predict(x_scaled);
            prob1 = clf1.predict_proba(x_scaled);

            #predict stance
            xtests.at[0,'text'] = tweet;
            x_scaled2 = count_vect2.transform(xtests.text);
            result2 = clf2.predict(x_scaled2);
            prob2 = clf2.predict_proba(x_scaled2);

            #predict sexual harassment category
            xtestc.at[0,'text'] = tweet;
            x_scaled3 = count_vect3.transform(xtestc.text);
            result3 = clf3.predict(x_scaled3);
            prob3 = clf3.predict_proba(x_scaled3);

            #the result is returned as an array with 1 index
            #the probability is returned as a 2D array, we want index 0 which has
            p0 = result1[0];
            p1 = result2[0];
            p2 = result3[0];
            p3 = prob1[0];
            p4 = prob2[0];
            p5 = prob3[0];

            #map the results to the output that the user wants to see
            if p0=='1':
                rel='Related';
                rel_prob = p3[0];
            if p0=='2':
                rel='Not Related';
                rel_prob = p3[0][1];

            if p1=='1':
                stance='Support';
                stance_prob = p4[0];
            if p1=='2':
                stance='Against';
                stance_prob = p4[1];
            if p1=='3':
                stance='Neutral';
                stance_prob = p4[3];

            if p2=='1':
                cat='Patronizing';
                cat_prob = p5[0];
            if p2=='2':
                cat='Unwanted Sexual Attention';
                cat_prob = p5[1];
            if p2=='3':
                cat='Predatory';
                cat_prob = p5[2];
            if p2=='4':
                cat='Not Enough Context';
                cat_prob = p5[3];

            rel_prob = round(rel_prob*100,2);
            stance_prob = round(stance_prob*100,2);
            cat_prob = round(cat_prob*100,2);

            probrel=str(rel_prob);
            probstance=str(stance_prob);
            probcat=str(cat_prob);
        else:
            return 'Tweet is too long';

    return '''<!DOCTYPE HTML>
    <html lang = "en">
    <head>
      <!-- basic.html -->
      <title>Thesis</title>
      <meta charset = "UTF-8" />
      <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="style.css">

    </head>
    <body>
      <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6 form-group">

      <h1>Enter your Tweet Below</h1>
      <p>
        Click submit to receive your classification.
      </p>

        <form name="tweet" method="POST">
        <label>Tweet</label>
        <textarea placeholder="Enter your tweet here... (limited to 280 characters)" rows="3" class="form-control" name="tweet" id="tweet" maxlength="280"></textarea><span id='remainingC'></span>
        <br/>
        <input type="submit" value="Submit">
      </form>
      </div>
    </div> <!--row-->
    <script src="scripty.js"></script>

  <div class="row">
  <div class="col-sm-3"></div>
  <div class="col-sm-6 form-group">
  <p>Your tweet was: {0}</p>
    <table>
    <col width="150">
    <col width="300">
    <col width="300">
    <col width="300">
    <tr>
        <th></th>
        <th>Relavance</th>
        <th>Stance</th>
        <th>Category</th>
    </tr>
    <tr>
        <th>Classification:</th>
        <th>{1}</th>
        <th>{2}</th>
        <th>{3}</th>
    </tr>
    <tr>
        <th>Probability:</th>
        <th>{4}%</th>
        <th>{5}%</th>
        <th>{6}%</th>
    </tr>
    </table>
    </div>
    </div><!--row-->
    </body>
    </html>'''.format(originalTweet,rel,stance,cat,probrel,probstance,probcat)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


#pickle
