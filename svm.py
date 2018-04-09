#NLP imports
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn import svm
from sklearn.metrics import classification_report


def svm_results_category(df):
    print('*******SEXUAL HARASSMENT CATEGORY*******');
    #fill in null values with the most common value
    #df = DataFrameImputer().fit_transform(df);
    #print(df);
    df=df[['id_str', 'text', 'category']];
    df=df.dropna();
    #vectorize
    count_vect=CountVectorizer();
    X = count_vect.fit_transform(df.text);
    print('\nX shape:')
    print(X.shape);
    Y = df.category;
    print('Y shape:')
    print(Y.shape);


    #split into training
    xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2);
    print('\nXtrain, Ytrain:');
    print (xtrain.shape, ytrain.shape);
    print('Xtest, Ytest:');
    print (xtest.shape, ytest.shape);

    print('\ntf-idf');
    #tfidf
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X)
    print('Xtrain tf-idf shape:');
    print(X_train_tfidf.shape);

    #algorithm
    clf=svm.SVC();
    clf.fit(xtrain,ytrain);

    #prediction
    ypredicted=clf.predict(xtest);

    #prints
    target_names = ['Patronizing', 'unwanted sexual attention', 'predatory', 'not enough context'];
    print(classification_report(ytest, ypredicted, target_names=target_names));

    #evaluate ourselves
    precision, recall, fscore, support = score(ytest, ypredicted)

def svm_results_stance(df):
    print('*******STANCE*******');
    #fill in null values with the most common value
    #df = DataFrameImputer().fit_transform(df);
    #print(df);
    df=df[['id_str', 'text', 'stance']];
    df=df.dropna();
    #vectorize
    count_vect=CountVectorizer();
    X = count_vect.fit_transform(df.text);
    print('\nX shape:')
    print(X.shape);
    Y = df.stance;
    print('Y shape:')
    print(Y.shape);


    #split into training
    xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2);
    print('\nXtrain, Ytrain:');
    print (xtrain.shape, ytrain.shape);
    print('Xtest, Ytest:');
    print (xtest.shape, ytest.shape);

    print('\ntf-idf');
    #tfidf
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X)
    print('Xtrain tf-idf shape:');
    print(X_train_tfidf.shape);

    #algorithm
    clf=svm.SVC();
    clf.fit(xtrain,ytrain);

    #prediction
    ypredicted=clf.predict(xtest);

    #prints
    target_names = ['Support','Against','Neutral'];
    print(classification_report(ytest, ypredicted, target_names=target_names));

    #evaluate ourselves
    precision, recall, fscore, support = score(ytest, ypredicted)

def svm_results_related(df):
    print('*******RELATED*******');
    #fill in null values with the most common value
    #df = DataFrameImputer().fit_transform(df);
    #print(df);
    df=df[['id_str', 'text', 'related']];
    df=df.dropna();
    #vectorize
    count_vect=CountVectorizer();
    X = count_vect.fit_transform(df.text);
    print('\nX shape:')
    print(X.shape);
    Y = df.related;
    print('Y shape:')
    print(Y.shape);


    #split into training
    xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2);
    print('\nXtrain, Ytrain:');
    print (xtrain.shape, ytrain.shape);
    print('Xtest, Ytest:');
    print (xtest.shape, ytest.shape);

    print('\ntf-idf');
    #tfidf
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X)
    print('Xtrain tf-idf shape:');
    print(X_train_tfidf.shape);

    #algorithm
    clf=svm.SVC();
    clf.fit(xtrain,ytrain);

    #prediction
    ypredicted=clf.predict(xtest);

    #prints
    target_names = ['Relevant','Irrelevant'];
    print(classification_report(ytest, ypredicted, target_names=target_names));

    #evaluate ourselves
    precision, recall, fscore, support = score(ytest, ypredicted);


###################################
def svm_results_category_noNEC(df):
    print('*******SEXUAL HARASSMENT CATEGORY - NO NEC*******');
    #fill in null values with the most common value
    #df = DataFrameImputer().fit_transform(df);
    #print(df);
    df=df[['id_str', 'text', 'category']];
    df=df.dropna();
    #vectorize
    count_vect=CountVectorizer();
    X = count_vect.fit_transform(df.text);
    print('\nX shape:')
    print(X.shape);
    Y = df.category;
    print('Y shape:')
    print(Y.shape);


    #split into training
    xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2);
    print('\nXtrain, Ytrain:');
    print (xtrain.shape, ytrain.shape);
    print('Xtest, Ytest:');
    print (xtest.shape, ytest.shape);

    print('\ntf-idf');
    #tfidf
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X)
    print('Xtrain tf-idf shape:');
    print(X_train_tfidf.shape);

    #algorithm
    clf=svm.SVC();
    clf.fit(xtrain,ytrain);

    #prediction
    ypredicted=clf.predict(xtest);

    #prints
    target_names = ['Patronizing', 'unwanted sexual attention', 'predatory'];
    print(classification_report(ytest, ypredicted, target_names=target_names));

    #evaluate ourselves
    precision, recall, fscore, support = score(ytest, ypredicted)
