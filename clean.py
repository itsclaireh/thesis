import re
import string
from nltk.corpus import stopwords
from html.parser import HTMLParser
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

#added the elipses and ? characters to python's punctuation set
punctuation = '!"$%&()*+,./:;<=>?@#[\]^_`{|}~'+'…'+'�';

#strip links
#https://stackoverflow.com/questions/8376691/how-to-remove-hashtag-user-link-of-a-tweet-using-regular-expression/8377440#8377440
def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text

#other help
#https://stackoverflow.com/questions/18146557/removing-escaped-entities-from-a-string-in-python

#remove URLs not caught with the initial strip
def remove_weird_urls(tweet):
    tweet = re.sub('(www|http).*?(org |net |edu |com |be |tt |me |ms |le)','',tweet);
    tweet = re.sub('(\s*)http(\s*)','',tweet);
    tweet = re.sub('(\s*)https(\s*)','',tweet);
    tweet = re.sub('(\s*)www(\s*)','',tweet);
    tweet = re.sub('(pic).*?(twitter).*?(com)','',tweet);
    return tweet;

#not used, decided to run linux command to remove non-UTF8 characters instead
def remove_nonUTF8(tweet):
    return tweet.decode('unicode_escape').encode('ascii','ignore');

#lemmatization
def stemmy(tweet):
    lemmy = WordNetLemmatizer();
    #stembro = SnowballStemmer('english');
    words=[];
    for word in tweet.split():
        word = word.strip()
        word = lemmy.lemmatize(word);
        words.append(word);
    return ' '.join(words);

    #porter_stemmer = PorterStemmer()
    #wordnet_lemmatizer = WordNetLemmatizer()

#apply other
#remove punctuation, username mentions, etc
def clean_tweet(tweet):
    tweet = tweet.lower();
    #tweet = remove_nonUTF8(tweet);
    tweet = strip_links(tweet);
    tweet = remove_weird_urls(tweet);

    entity_prefixes = ['@']
    for separator in punctuation:
        if separator not in entity_prefixes :
            tweet = tweet.replace(separator,' ')
    words = []
    for word in tweet.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                if word not in stopwords.words('english'):
                    words.append(word)
    processed =  ' '.join(words)
    #condense contractions into a word instead of splitting on it
    final = [];
    for token in processed.split(' '):
        part=token.replace('\'', '');
        final.append(part);
    return ' '.join(final);


#not used, decided to loop in the main file instead of here
def clean_all(tweet):
    for t in tweet:
        t=clean_tweet(t);

    return tweet;
