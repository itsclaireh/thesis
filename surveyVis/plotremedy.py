from barPreventing import barchartPrev
from barReporting import barchartRep
from barStackReporting import barStackRep
from barStackPreventing import barStackPrev
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
#import matplotlib.backends.backend._pdf

def socialMediaResults(df,no):
    return df.loc[df['socialMedia']==no,['socialMedia','socialMediaOption','reportingSH','preventingSH']];

def socialMediaResults2(df,no):
    return df.loc[df['socialMedia']==no,['age','socialMedia','socialMediaOption','reportingSH','preventingSH']];

df = pd.read_csv('remedy.csv',header=None,index_col=None,encoding='utf8',dtype='str');
columns = ['age','gender','genderOption','socialMedia','socialMediaOption','remedy','improvementsOption'];
df.columns = np.ravel(columns);

df=df.replace(np.nan,'',regex=True)

advertisement=0;
stricterRegulation=0;
newsFeedAdjust=0;
automaticallyArchive=0;
connectVictims=0;

for i, row in df.iterrows():
    if df.at[i,'remedy']=='1':
        advertisement+=1;
        print('hi')
print(advertisement);
