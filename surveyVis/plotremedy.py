from barPreventing import barchartPrev
from barReporting import barchartRep
from barStackReporting import barStackRep
from barStackPreventing import barStackPrev
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.font_manager import FontProperties

#import matplotlib.backends.backend._pdf

df = pd.read_csv('remedy.csv',header=None,index_col=None,encoding='utf8',dtype='str');
columns = ['age','gender','genderOption','socialMedia','socialMediaOption','remedy','improvementsOption'];
df.columns = np.ravel(columns);

df=df.replace(np.nan,'',regex=True)

advertisement = stricterRegulation = newsFeedAdjust = automaticallyArchive = connectVictims = other = invalid = 0;
f_advertisement = f_stricterRegulation = f_newsFeedAdjust = f_automaticallyArchive = f_connectVictims = f_other = f_invalid = 0;
m_advertisement = m_stricterRegulation = m_newsFeedAdjust = m_automaticallyArchive = m_connectVictims = m_other = m_invalid = 0;
o_advertisement = o_stricterRegulation = o_newsFeedAdjust = o_automaticallyArchive = o_connectVictims = o_other = o_invalid = 0;

sums=df[['gender','remedy','improvementsOption']];
sums = sums.dropna();
df=df.replace(np.nan,'',regex=True);

for i, row in sums.iterrows():
    '''
    advertisement = advertisement+1 if '1' in row.remedy else advertisement;
    stricterRegulation = stricterRegulation+1 if '1' in row.remedy else stricterRegulation;
    newsFeedAdjust = newsFeedAdjust+1 if '1' in row.remedy else newsFeedAdjust;
    automaticallyArchive = automaticallyArchive+1 if '1' in row.remedy else automaticallyArchive;
    connectVictims = connectVictims+1 if '1' in row.remedy else connectVictims;
    other = other+1 if '1' in row.remedy else other;
    '''

    if row.gender == '1':
        m_advertisement = m_advertisement+1 if '1' in row.remedy else m_advertisement;
        m_stricterRegulation = m_stricterRegulation+1 if '2' in row.remedy else m_stricterRegulation;
        m_newsFeedAdjust = m_newsFeedAdjust+1 if '3' in row.remedy else m_newsFeedAdjust;
        m_automaticallyArchive = m_automaticallyArchive+1 if '4' in row.remedy else m_automaticallyArchive;
        m_connectVictims = m_connectVictims+1 if '5' in row.remedy else m_connectVictims;
        m_other = m_other+1 if '6' in row.remedy else m_other;

    if row.gender == '2':
        f_advertisement = f_advertisement+1 if '1' in row.remedy else f_advertisement;
        f_stricterRegulation = f_stricterRegulation+1 if '2' in row.remedy else f_stricterRegulation;
        f_newsFeedAdjust = f_newsFeedAdjust+1 if '3' in row.remedy else f_newsFeedAdjust;
        f_automaticallyArchive = f_automaticallyArchive+1 if '4' in row.remedy else f_automaticallyArchive;
        f_connectVictims = f_connectVictims+1 if '5' in row.remedy else f_connectVictims;
        f_other = f_other+1 if '6' in row.remedy else f_other;

    if row.gender == '3' or row.gender=='4':
        o_advertisement = o_advertisement+1 if '1' in row.remedy else o_advertisement;
        o_stricterRegulation = o_stricterRegulation+1 if '2' in row.remedy else o_stricterRegulation;
        o_newsFeedAdjust = o_newsFeedAdjust+1 if '3' in row.remedy else o_newsFeedAdjust;
        o_automaticallyArchive = o_automaticallyArchive+1 if '4' in row.remedy else o_automaticallyArchive;
        o_connectVictims = o_connectVictims+1 if '5' in row.remedy else o_connectVictims;
        o_other = o_other+1 if '6' in row.remedy else o_other;

    items = ['1','2','3','4','5','6'];
    if any(x in row.remedy for x in items) == False:
        invalid+=1;

advertisement = f_advertisement + m_advertisement + o_advertisement;
stricterRegulation = f_stricterRegulation + m_stricterRegulation + o_stricterRegulation;
newsFeedAdjust = f_newsFeedAdjust + m_newsFeedAdjust + o_newsFeedAdjust;
automaticallyArchive = f_automaticallyArchive + m_automaticallyArchive + o_automaticallyArchive;
connectVictims = f_connectVictims + m_connectVictims + o_connectVictims;

n=5;
dataAll = np.array([advertisement,stricterRegulation,newsFeedAdjust,automaticallyArchive,connectVictims]);
dataMen = np.array([m_advertisement,m_stricterRegulation,m_newsFeedAdjust,m_automaticallyArchive,m_connectVictims]);
dataWomen = np.array([f_advertisement,f_stricterRegulation,f_newsFeedAdjust,f_automaticallyArchive,f_connectVictims]);
dataOther = np.array([o_advertisement,o_stricterRegulation,o_newsFeedAdjust,o_automaticallyArchive,o_connectVictims]);

print(dataAll);
print(dataMen);
print(dataWomen);
print(dataOther);

#names = ['Advertisement', 'Stricter Regulation', 'News Feed Adjustment', 'Automatically Archive', 'Connect Victims'];
names = ['Connect Victims','Automatically Archive', 'News Feed Adjustment', 'Stricter Regulation','Advertisement'];
x_pos = [i for i, _ in enumerate(names)];

ind = np.arange(n);
bar_width = 0.2;

plt.barh(ind, dataMen,bar_width,color='#450a5cff',label='Men');
plt.barh(ind-bar_width, dataWomen,bar_width,color='#2d6e8eff',label='Women');
plt.barh(ind-bar_width*2,dataOther,bar_width,color='#49be6eff',label='Other');

#plt.barh(ind, dataAll,width,color='#e1e329ff',label='All')
plt.ylabel('Improvement Suggestions');
plt.xlabel('Number of Responses per Gender Identity');
plt.title('Improvements to Social Media');
plt.yticks(ind-bar_width,names);
plt.legend(loc='lower right');
plt.tight_layout();

plt.savefig("ImprovementsBar.pdf", bbox_inches="tight");
plt.savefig("ImprovementsBar.png", bbox_inches="tight")
plt.show();

total = dataMen+dataWomen+dataOther;
pdataMen = np.true_divide(dataMen,total )*100;
pdataWomen = np.true_divide(dataWomen,total  )*100;
pdataOther = np.true_divide(dataOther,total)*100;

new = plt.bar(x_pos,pdataMen,width=0.8,label='Men',color='#450a5cff',bottom=pdataWomen+pdataOther);
new2 = plt.bar(x_pos,pdataWomen,width=0.8,label='Women',color='#2d6e8eff',bottom=pdataOther);
new3 = plt.bar(x_pos,pdataOther,width=0.8,label='Other',color='#49be6eff');

plt.xticks(x_pos,names,rotation=45, horizontalalignment='right');
plt.ylabel('Number of Responses per Gender Identity');
plt.xlabel('Improvement Suggestions');
plt.legend(loc='upper right');
plt.title('Improvements to Social Media');
plt.tight_layout();

plt.savefig("ImprovementsStack.pdf", bbox_inches="tight");
plt.savefig("ImprovementsStack.png", bbox_inches="tight")
plt.show();
