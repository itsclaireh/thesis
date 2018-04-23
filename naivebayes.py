#NLP imports
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
import numpy as np


def nb_results(df, classLabel, y):
    print('\t\t\t*******NAIVE BAYES*******');
    print('\t\t\tCLASS:\t{0}'.format(classLabel));

    #fill in null values with the most common value
    #df = DataFrameImputer().fit_transform(df);
    #print(df);
    df=df[['id_str', 'text', classLabel]];
    df=df.dropna();

    #vectorize
    count_vect=CountVectorizer(); ##pass parameters here
    X = count_vect.fit_transform(df.text);
    Y = df[[classLabel]];
    Y = np.ravel(Y);

    #split into training
    xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2);

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
        target_names = ['Patronizing', 'unwanted sexual attention', 'predatory', 'not enough context'];
    elif classLabel == 'stance':
        target_names = ['Support','Against','Neutral'];
    elif classLabel == 'related':
        target_names = ['Relevant','Irrelevant'];
    else:
        target_names = ['Patronizing', 'unwanted sexual attention', 'predatory'];

    print(classification_report(ytest, ypredicted, target_names=target_names));
