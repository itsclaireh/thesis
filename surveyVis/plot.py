from preventing import barchartPrev
from reporting import barchartRep

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import csv
#import matplotlib.backends.backend._pdf

def socialMediaResults(df,no):
    return df.loc[df['socialMedia']==no,['socialMedia','socialMediaOption','reportingSH','preventingSH']];

def socialMediaResults2(df,no):
    return df.loc[df['socialMedia']==no,['age','socialMedia','socialMediaOption','reportingSH','preventingSH']];

df = pd.read_csv('survey-num.csv',header=None,index_col=None,encoding='utf8',dtype='str');
#df.columns=['id_str','text','related','stance','category'];
columns1=['startDate','endDate','responseType','progress','duration','finished','recordedDate','responseID','distributionChannel','language','consent']
columns2=['age','gender','genderOption','staringLeering','catcalling','pinchingPoking','sexistComments','inappropriateDrawings','messagesStrangers','lewdRemarks','obsceneGestures','repeatedMessages','personalQuestions','stalkingHarassment','gropingTouching','unsolicitedPhotos','behaviorOptionSeverity','behaviorOptionText','socialMedia','socialMediaOption','preventingSH','reportingSH','improvments','improvementsOption'];
columns=columns1+columns2;
df.columns = np.ravel(columns);

metadata=df[columns1];
metadata = metadata.replace(np.nan,'',regex=True)
#print(metadata);

responses=df[columns2];
responses = responses.replace(np.nan,'',regex=True)
#print(responses);

face = socialMediaResults(responses,'1');
yout = socialMediaResults(responses,'2');
insta = socialMediaResults(responses,'3');
twit = socialMediaResults(responses,'4');
snap = socialMediaResults(responses,'5');
redd = socialMediaResults(responses,'6');
tumbl = socialMediaResults(responses,'7');
other = responses.loc[responses['socialMediaOption']!='',['socialMediaOption','preventingSH','reportingSH']];

barchartPrev(face,yout,insta,twit,snap,redd,tumbl,other);
barchartRep(face,yout,insta,twit,snap,redd,tumbl,other);


'''
answer = df[['gender','improvementsOption']];
#print(answer);
answer = answer.replace(np.nan,'',regex=True)
ans = answer.loc[answer['improvementsOption']!='',['gender','improvementsOption']];

print('Total Responses:');
print(len(responses))
qualitative=ans.as_matrix();

#for i, row in ans.iterrows():
    #print(row.improvementsOption);
    #temp=ans.values;
    #print(temp)
    #qualitative = np.concatenate([qualitative,temp]);
    #print('\n');

with open('improvementsOptions.csv','w+',newline='') as csvfile:
    csvWriter = csv.writer(csvfile,delimiter=',');
    #for i in range(0,len(qualitative)):
    for line in qualitative:
        csvWriter.writerow(line);
'''
