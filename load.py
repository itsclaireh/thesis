import csv
import numpy as np
import urllib.request
import scipy
import pandas as pd
from io import StringIO
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
import string

import spacy
spacy.load('en_core_web_sm')
import spacy.en
from spacy.lang.en import English
nlp=spacy.load('en')

import re
#from many_stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import chain


from nltk.classify import NaiveBayesClassifier, accuracy


#url = "https://raw.githubusercontent.com/claireballoon/thesis/master/TestData.tsv"

#with urllib.request.urlopen("https://raw.githubusercontent.com/claireballoon/thesis/master/TestData.tsv") as url:
#    raw_data = url.read().decode('utf-8')

#put our file into an array
#content=[];
#with open('MeTooData.csv','r') as textfile:
#    for line in (list(csv.reader(textfile))):
#        content.append(line);


#*****BEGIN******
# We have a problem - participants labeled tweets in a Google Sheet...
# This limits our export options. Unfortunately, the tweets themselves
# could contain any of the delimiters we desire to use. Therefore, we must`
# strip the first column (ids), then strip the labeling/categorization (rel, st, cat)
# and then we can assume what is leftover is the tweet, even if it contains a delimeter


#variables for this process
ids=[];
rel=[];
st=[];
cat=[];
counter=0;
currentTweet=[];
contentsWithoutLabels=[];

#take the categories, which are always the last items
#so we need to go through each row in reverse this time
with open('MeTooData.csv','r') as textfile:
    for row in (list(csv.reader(textfile))):
        counter=-1;
        for i in reversed(row):
            counter=counter+1;
            #if the counter is 0, 1, or 2 then we are looking at relevant/stance/category
            if counter==2:
                rel.append(i);
            elif counter==1:
                st.append(i);
            elif counter==0:
                cat.append(i);

            #if we've reached the end of the row, it's the ID
            elif (len(row)-1)==counter:
                ids.append(i);

            #everything else is the tweet!!
            #we want to keep the tweets as an array of strings, so
            #append the contents (separated by the delimeter)
            #to a 1D array
            else:
                currentTweet.append(i);

        #now add that array to the list of tweet contents without labels
        contentsWithoutLabels.append(currentTweet.pop());

#put it all back together
#but only if all our lists are of the same length
length=len(ids);
if (len(contentsWithoutLabels) == length and len(rel) == length):
    df1 = pd.DataFrame(np.array(ids));
    df2 = pd.DataFrame(np.array(contentsWithoutLabels));
    df3 = pd.DataFrame(np.array(rel));
    df4 = pd.DataFrame(np.array(st));
    df5 = pd.DataFrame(np.array(cat));
    data=pd.concat([df1,df2,df3,df4,df5],axis=1);
    data.columns=['id_str','text','related','stance','category'];
    #print(data);
else:
    print('Data mismatch');

# ***** Cleaning the data ******

words = [];
tempTweet = [];

cleanedTweet=[];
tweetTokenizedBySpaces=[];


punctuation = '!"$%&()*+,./:;<=>?@[\]^_`{|}~'+'…'+'�';
#https://stackoverflow.com/questions/8376691/how-to-remove-hashtag-user-link-of-a-tweet-using-regular-expression/8377440#8377440
def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text

def clean_tweet(tweet):
        strip_links(tweet)
        tweet = tweet.lower();
        entity_prefixes = ['@']
        for separator in punctuation:
            if separator not in entity_prefixes :
                tweet = tweet.replace(separator,' ')
        words = []
        for word in tweet.split():
            word = word.strip()
            if word:
                if word[0] not in entity_prefixes:
                    words.append(word)
        return ' '.join(words)

def lemmatization(tweet):
    nlp = spacy.en.English();
    doc = nlp(tweet);
    lemmata = [token.lemma_ for token in doc];
    return lemmata;

for tweet in contentsWithoutLabels:
    tweet = clean_tweet(tweet);
    tweet = lemmatization(tweet);
    tweetTokenizedBySpaces.append(tweet.split());

for tweet in tweetTokenizedBySpaces:
    table = str.maketrans('', '', punctuation);
    cleanedTweet.append([w.translate(table) for w in words]);






#count_vect = CountVectorizer();
#X_train_counts = count_vect.fit_transform(data)
#X_train_counts.shape;

#print(X_train_counts);
