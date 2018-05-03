#My Functions
from DataFrameImputer import *;
from clean import clean_tweet, stemmy;
from compare import compare_and_load_datasets, remove_NEC, load_file;
from svm import svm_results,svm_results_reduction;
from naivebayes import nb_results;
import pandas as pd

def printSizes(women):
    women_cat1 = women.loc[df.category=='1'];
    women_cat2 = women.loc[df.category=='2'];
    women_cat3 = women.loc[df.category=='3'];
    women_cat4 = women.loc[df.category=='4'];

    print('\nTOTAlS:');
    print('Patronizing:\t\t\t{0}'.format(len(women_cat1)));
    print('Unwanted Sexual Attention:\t{0}'.format(len(women_cat2)));
    print('Predatory:\t\t\t{0}'.format(len(women_cat3)));
    print('Not Enough Context:\t\t{0}'.format(len(women_cat4)));

    women_rel1 = women.loc[df.related=='1'];
    women_rel2 = women.loc[df.related=='2'];
    print('\nTOTAlS:');
    print('Relevant:\t\t{0}'.format(len(women_rel1)));
    print('Irrelevant:\t\t{0}'.format(len(women_rel2)));

    women_st1 = women.loc[df.stance=='1'];
    women_st2 = women.loc[df.stance=='2'];
    women_st3 = women.loc[df.stance=='3'];
    print('\nTOTAlS:');
    print('Support:\t\t{0}'.format(len(women_st1)));
    print('Against:\t\t{0}'.format(len(women_st2)));
    print('Neutral:\t\t{0}'.format(len(women_st3)));

#load files
file1 = 'data/MeTooMen.csv';
file2 = 'data/MeTooWomen.csv';
d = compare_and_load_datasets(file1, file2);

supp = load_file('data/supplemental.csv');
df=pd.concat([d,supp]);

supp2 = load_file('data/suppTweetsNoID.csv');
df=pd.concat([df,supp2]);

men = load_file(file1);
women = load_file(file2);


#clean tweets
for i, row in df.iterrows():
  if row.text:
      df.at[i,'text']=clean_tweet(row.text);
      #df.set_value(i,'text',stemmy(row.text));
      #men.set_value(i, 'text',clean_tweet(row.text));
      #women.set_value(i, 'text',clean_tweet(row.text));
      #df.at[df.index[i-2], 'text'] = clean_tweet(row.text);

print('\n');

#comment/uncomment rates
#used to test the different results of changing certain variables

#rates = [0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50];
rates = [0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95];
#rates = [0,.1,.15,.2,.25,.3];
#rates = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000];
#rates = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150];


svm_results_reduction(df, 'related',1);
svm_results_reduction(df, 'stance',1);
svm_results_reduction(df, 'category',10);
nb_results(df, 'related',i);
nb_results(df, 'stance',i);
nb_results(df, 'category',i);
