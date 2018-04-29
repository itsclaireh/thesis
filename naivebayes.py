#NLP imports
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn import preprocessing


def nb_results(df, classLabel, variabl):
    print('\t\t\t*******NAIVE BAYES*******');
    print('\t\t\tCLASS:\t{0}'.format(classLabel));


    print('\t\tVariable:\t{0}%'.format(variabl));
    if classLabel=='related':
        df= df.drop(df.query('related in ["1"]').sample(frac=.65,random_state=1).index);
        df_related = df.loc[df.related=='1'];
        print('\t\tRelated:\t{0}'.format(len(df_related)));
    elif classLabel=='stance':
        df= df.drop(df.query('stance in ["1"]').sample(frac=.2,random_state=2).index);
        df_support = df.loc[df.stance=='1'];
        print('\t\tSupport:\t{0}'.format(len(df_support)));
    elif classLabel =='category':
        df= df.drop(df.query('category in ["4"]').sample(frac=0,random_state=3).index);
        df_NEC = df.loc[df.category=='4'];
        print('\t\tNEC:\t{0}'.format(len(df_NEC)));

    #fill in null values with the most common value
    #df = DataFrameImputer().fit_transform(df);
    #print(df);
    df=df[['id_str', 'text', classLabel]];
    df=df.dropna();

    #vectorize
    count_vect=CountVectorizer(strip_accents='unicode'); ##pass parameters here
    X = count_vect.fit_transform(df.text);
    Y = df[[classLabel]];
    Y = np.ravel(Y);
    print('\t\tTotal Samples:\t{0}'.format(len(Y)));
    names = count_vect.get_feature_names();
    print('\t\tFeatures:\t{0}'.format(len(names)));
    #split into training
    xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2,random_state=0,stratify=Y);


    tfidf_transformer = TfidfTransformer();
    X_tfidf = tfidf_transformer.fit_transform(xtrain);

    clf = MultinomialNB();
    clf.fit(X_tfidf,ytrain);

    #prediction
    ypredicted=clf.predict(xtest);

    '''
    print('X Shape:\t{0}'.format(X.shape));
    print('Y Shape:\t{0}'.format(Y.shape));
    print('XTrain, YTrain:\t{0}'.format(xtrain.shape, ytrain.shape));
    print('XTest, YTest:\t{0}'.format(xtest.shape, ytest.shape));
    print('X TFIDF:\t{0}'.format(X_tfidf.shape));
    '''

    if classLabel == 'category':
        target_names = ['Patronizing', 'Unwanted Sexual Attention', 'Predatory', 'Not Enough Context'];
    elif classLabel == 'stance':
        target_names = ['Support','Against','Neutral'];
    elif classLabel == 'related':
        target_names = ['Relevant','Irrelevant'];
    else:
        print('Something is Wrong');

    print(classification_report(ytest, ypredicted, target_names=target_names));
    print('\t\tAccuracy:\t{0:.3f}\n'.format(accuracy_score(ytest, ypredicted)*100));
