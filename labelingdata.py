import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from compare import compare_and_load_datasets, remove_NEC, load_file;
from matplotlib import rc
from matplotlib.font_manager import FontProperties



#print(women);
#print(men);
# purple - #450a5cff
# blue - #2d6e8eff
# green - #49be6eff
# lime - #e1e329ff
#classes=['Relevant','Irrelevant','Support','Against','Neutral','Patronizing','Unwanted Sexual Attention','Predatory','Not Enough Context'];
#classes=['Not Enough Context','Predatory','Unwanted Sexual Attention','Patronizing','Neutral','Against','Support','Irrelevant','Relevant'];
rel = ['Relevant','Irrelevant','Left Blank'];
womenRel = [4588,340,72];
menRel = [4576,132,292];

pos = [i for i, _ in enumerate(rel)];

bar_width = 0.35;
opacity=0.35;
ind = np.arange(len(rel));
bar1 = plt.barh(ind,womenRel,bar_width,color='#e1e329ff',label='Women');
bar2 = plt.barh(ind-bar_width,menRel,bar_width,color='#2d6e8eff',label='Men');

plt.yticks(ind-bar_width/2,rel);
plt.ylabel('Relevance')
plt.xlabel('Number of Tweets Labeled')
plt.title('Tweets Labeled Across Gender - Relevance')
plt.legend(loc='best')
plt.tight_layout();
plt.savefig("surveyVis/pdfs/labelRel.pdf", bbox_inches="tight");
plt.savefig("surveyVis/pngs/labelRel.png", bbox_inches="tight");
fig1 = plt.show()


sta = ['Support','Against','Neutral',' Left Blank'];
womenStance = [3961,150,119,770];
menStance = [3860,112,44,984];


pos = [i for i, _ in enumerate(sta)];
bar_width = 0.35;
opacity=0.35;
ind = np.arange(len(sta));
bar1 = plt.barh(ind,womenStance,bar_width,color='#e1e329ff',label='Women');
bar2 = plt.barh(ind-bar_width,menStance,bar_width,color='#2d6e8eff',label='Men');

plt.yticks(ind-bar_width/2,sta);
plt.ylabel('Stance')
plt.xlabel('Number of Tweets Labeled')
plt.title('Tweets Labeled Across Gender - Stance')
plt.legend(loc='best')
plt.tight_layout();
plt.savefig("surveyVis/pdfs/labelStance.pdf", bbox_inches="tight");
plt.savefig("surveyVis/pngs/labelStance.png", bbox_inches="tight");
fig2 = plt.show()



cat = ['Patronizing','Unwanted Sexual Attention','Predatory','Not Enough Context','Blank'];
womenCat = [96,82,372,2367,2083];
menCat = [60,166,370,2161,2243];

pos = [i for i, _ in enumerate(cat)];

bar_width = 0.35;
opacity=0.35;
ind = np.arange(len(cat));
bar1 = plt.barh(ind,womenCat,bar_width,color='#e1e329ff',label='Women');
bar2 = plt.barh(ind-bar_width,menCat,bar_width,color='#2d6e8eff',label='Men');

plt.yticks(ind-bar_width/2,cat);
plt.ylabel('Category')
plt.xlabel('Number of Tweets Labeled')
plt.title('Tweets Labeled Across Gender - Type')
plt.legend(loc='best')
plt.tight_layout();
plt.savefig("surveyVis/pdfs/labelCat.pdf", bbox_inches="tight");
plt.savefig("surveyVis/pngs/labelCat.png", bbox_inches="tight");
fig3 = plt.show()


classes=['Relevant','Irrelevant','Support','Against','Neutral','Patronizing','Unwanted Sexual Attention','Predatory','Not Enough Context'];
women = [4588,340,3961,150,119,96,82,372,2367];
men = [4576,132,3860,112,44,60,166,370,2161];

pos = [i for i, _ in enumerate(classes)];

bar_width = 0.35;
opacity=0.35;
ind = np.arange(len(classes));
bar1 = plt.barh(ind,women,bar_width,color='#e1e329ff',label='Women');
bar2 = plt.barh(ind-bar_width,men,bar_width,color='#2d6e8eff',label='Men');

plt.yticks(ind-bar_width/2,classes);
plt.ylabel('Class Labels')
plt.xlabel('Tweets Labeled')
plt.title('Tweets Labeled Across Gender - All')
plt.legend(loc='best')
plt.tight_layout();
plt.savefig("surveyVis/pdfs/labelTotal.pdf", bbox_inches="tight");
plt.savefig("surveyVis/pngs/labelTotal.png", bbox_inches="tight");
fig4 = plt.show()
