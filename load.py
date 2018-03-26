import csv
import numpy as np
import urllib.request
import scipy
import pandas as pd
from io import StringIO
from sklearn.preprocessing import MinMaxScaler

#url = "https://raw.githubusercontent.com/claireballoon/thesis/master/TestData.tsv"

#put our file into an array
content=[];
with open('test.csv','r') as textfile:
    for line in (list(csv.reader(textfile))):
        content.append(line);

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
with open('testcrap.csv','r') as textfile:
    for row in (list(csv.reader(textfile))):
        counter=-1;
        for i in reversed(row):
            counter=counter+1;
            #if the counter is 0, 1, or 2 then we are looking at relevant/stance/category
            if counter==0:
                rel.append(i);
            #elif counter==1:
            #    st.append(i):
            #elif: counter==1:
            #    cat.append(i);

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

#for x in reversed(contentsWithoutLabels):
#    print('['+x+']');

length=len(ids);
#put it all back together
df1 = pd.DataFrame(np.array(ids));
df2 = pd.DataFrame(np.array(contentsWithoutLabels));
df3 = pd.DataFrame(np.array(rel));
data=pd.concat([df1,df2,df3],axis=1);
data.columns=['id_str','text','related'];
print(data);

#with urllib.request.urlopen("https://raw.githubusercontent.com/claireballoon/thesis/master/TestData.tsv") as url:
#    raw_data = url.read().decode('utf-8')

#dataset = np.loadtxt(raw_data, delimiter="\t")
#X = dataset[:,0:1]
#y = dataset[:,2]


#categories=['1','2']

#print(names)
#print(dataset)
