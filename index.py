#NLP imports
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

def printResults(results, probability):

    related='';
    stance='';
    cat='';
    prob1 = prob2 = prob3 =0;

    if results[0]=='1':
        related='Related';
        prob1 = probability[0][0];
    elif results[0]=='2':
        related='Not Related';
        prob1 = probability[0][1];

    if results[1]=='1':
        stance='Support';
        prob2 = probability[1][0];
    elif results[1]=='2':
        stance='Against';
        prob2 = probability[1][1];
    elif results[1]=='3':
        stance='Neutral';
        prob2 = probability[1][3];

    if results[2]=='1':
        cat='Patronizing';
        prob3 = probability[2][0];
    elif results[2]=='2':
        cat='Unwanted Sexual Attention';
        prob3 = probability[2][1];
    elif results[2]=='3':
        cat='Predatory';
        prob3 = probability[2][2];
    elif results[2]=='4':
        cat='Not Enough Context';
        prob3 = probability[2][3];


        print('\t\tRELATED\t\tSTANCE\t\tCATEGORY')
        print('Category:\t{0}\t\t\t{1}\t\t\t{2}'.format(related, stance, cat));
        print('Probability:\t{0:.2f}%\t\t\t{1:.2f}%\t\t\t{2:.2f}%\n'.format(prob1*100, prob2*100, prob3*100));


file1 = 'data/MeTooMen.csv';
file2 = 'data/MeTooWomen.csv';
d = compare_and_load_datasets(file1, file2);

supp = load_file('data/supplemental.csv');
df=pd.concat([d,supp]);

supp2 = load_file('data/suppTweetsNoID.csv');
df=pd.concat([df,supp2]);


#clean tweets
for i, row in df.iterrows():
  if row.text:
      df.at[i,'text']=clean_tweet(row.text);


print('\n\n\t\t*******SVM*******');
dfrel= df.drop(df.query('related in ["1"]').sample(frac=.55,random_state=1).index);
print('\t\tRelated:\t{0}'.format(len(dfrel.loc[dfrel.related=='1'])));
print('\t\tNot Related:\t{0}'.format(len(dfrel.loc[dfrel.related=='2'])));
dfstance= df.drop(df.query('stance in ["1"]').sample(frac=.2,random_state=2).index);
print('\t\tSupport:\t{0}'.format(len(dfstance.loc[dfstance.stance=='1'])));
print('\t\tAgainst:\t{0}'.format(len(dfstance.loc[dfstance.stance=='2'])));
print('\t\tNeutral:\t{0}'.format(len(dfstance.loc[dfstance.stance=='3'])));
dfcat= df.drop(df.query('category in ["4"]').sample(frac=0.0,random_state=3).index);
print('\t\tPatronizing:\t{0}'.format(len(dfcat.loc[dfcat.category=='1'])));
print('Unwanted Sexual Attention:\t{0}'.format(len(dfcat.loc[dfcat.category=='2'])));
print('\t\tPredatory:\t{0}'.format(len(dfcat.loc[dfcat.category=='3'])));
print('\tNot Enough Context:\t{0}'.format(len(dfcat.loc[dfcat.category=='4'])));


dfrel=dfrel[['id_str', 'text', 'related']];
dfstance=dfstance[['id_str', 'text', 'stance']];
dfcat=dfcat[['id_str', 'text', 'category']];

dfrel=dfrel.dropna();
dfstance = dfstance.dropna();
dfcat=dfcat.dropna();

count_vect=CountVectorizer(strip_accents='unicode');
count_vect2=CountVectorizer(strip_accents='unicode');
count_vect3=CountVectorizer(strip_accents='unicode');

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


tfidf_transformer = TfidfTransformer();
X_train_tfidf = tfidf_transformer.fit_transform(Xr)
tfidf_transformer2 = TfidfTransformer();
X_train_tfidf2 = tfidf_transformer.fit_transform(Xs)
tfidf_transformer3 = TfidfTransformer();
X_train_tfidf3 = tfidf_transformer.fit_transform(Xc)

linclf1=LinearSVC(random_state=0, C=1,loss="hinge");
clf1 = CalibratedClassifierCV(linclf1);
clf1.fit(X_train_tfidf,Yr);

linclf2=LinearSVC(random_state=0, C=1,loss="hinge");
clf2 = CalibratedClassifierCV(linclf2);
clf2.fit(X_train_tfidf2,Ys);

linclf3=LinearSVC(random_state=0, C=10,loss="hinge");
clf3 = CalibratedClassifierCV(linclf3);
clf3.fit(X_train_tfidf3,Yc);


print('\n');
go = 'yes';
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
while go=='yes':
    tweet = input('What is your tweet? \n');
    tweet = clean_tweet(tweet);

    xtestr.at[0,'text'] = tweet;
    x_scaled = count_vect.transform(xtestr.text);
    result1 = clf1.predict(x_scaled);
    prob1 = clf1.predict_proba(x_scaled);

    xtests.at[0,'text'] = tweet;
    x_scaled2 = count_vect2.transform(xtests.text);
    result2 = clf2.predict(x_scaled2);
    prob2 = clf2.predict_proba(x_scaled2);

    xtestc.at[0,'text'] = tweet;
    x_scaled3 = count_vect3.transform(xtestc.text);
    result3 = clf3.predict(x_scaled3);
    prob3 = clf3.predict_proba(x_scaled3);

    result = [result1[0],result2[0],result3[0]];
    probability = [prob1[0],prob2[0],prob3[0]];

    printResults(result,probability);

    go = input('Do you want to enter another tweet? (type \'yes\') ');
