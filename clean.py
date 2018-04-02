import re

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

def clean_all(tweet):
    for t in tweet:
        t=clean_tweet(t);

    return tweet;
