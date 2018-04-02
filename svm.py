#My Functions
from DataFrameImputer import *;
from clean import clean_tweet;
from compare import compare_and_load_datasets;

#NLP imports
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn import svm


file1 = 'MeTooMen.csv';
file2 = 'MeTooWomen.csv';
df = compare_and_load_datasets(file1, file2);

#clean tweets
for i, row in df.iterrows():
  if row.text:
      df.set_value(i, 'text', clean_tweet(row.text));

#fill in null values with the most common value
df = DataFrameImputer().fit_transform(df);
print(df);

#vectorize
count_vect=CountVectorizer();
X = count_vect.fit_transform(df.text);
print(X.shape);
Y = df.category;

#split into training
print(Y.shape);
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2);

print (xtrain.shape, ytrain.shape);
print (xtest.shape, ytest.shape);

#tfidf
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X)
print(X_train_tfidf.shape);

#algorithm
clf=svm.SVC();
clf.fit(xtrain,ytrain);

#prediction
predicted=clf.predict(xtest);

#evaluate ourselves
precision, recall, fscore, support = score(ytest, predicted)

print('')

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))
