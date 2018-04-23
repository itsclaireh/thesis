#My Functions
from DataFrameImputer import *;
from clean import clean_tweet;
from compare import compare_and_load_datasets, remove_NEC, load_file;
from svm import svm_results;
from naivebayes import nb_results;

import pandas as pd

file1 = 'data/MeTooMen.csv';
file2 = 'data/MeTooWomen.csv';
d = compare_and_load_datasets(file1, file2);

supp = load_file('data/supplemental.csv');
df=pd.concat([d,supp]);
#print(df);

#clean tweets
for i, row in df.iterrows():
  if row.text:
      df.set_value(i, 'text', clean_tweet(row.text));
      #df.at[df.index[i-2], 'text'] = clean_tweet(row.text);

print('\nPRINTING RESULTS:');


df_cat1 = df.loc[df.category=='1'];
df_cat2 = df.loc[df.category=='2'];
df_cat3 = df.loc[df.category=='3'];
df_cat4 = df.loc[df.category=='4'];

print('\nTOTAlS:');
print('Patronizing:\t\t\t{0}'.format(len(df_cat1)));
print('Unwanted Sexual Attention:\t{0}'.format(len(df_cat2)));
print('Predatory:\t\t\t{0}'.format(len(df_cat3)));
print('Not Enough Context:\t\t{0}'.format(len(df_cat4)));

df_rel1 = df.loc[df.related=='1'];
df_rel2 = df.loc[df.related=='2'];
print('\nTOTAlS:');
print('Relevant:\t\t{0}'.format(len(df_rel1)));
print('Irrelevant:\t\t{0}'.format(len(df_rel2)));

df_st1 = df.loc[df.stance=='1'];
df_st2 = df.loc[df.stance=='2'];
df_st3 = df.loc[df.stance=='3'];
print('\nTOTAlS:');
print('Support:\t\t{0}'.format(len(df_st1)));
print('Against:\t\t{0}'.format(len(df_st2)));
print('Neutral:\t\t{0}'.format(len(df_st3)));


print('\n');


#svm_results(df, 'related');
#svm_results(df, 'stance');
svm_results(df, 'category');

#nb_results(df, 'related');
#nb_results(df, 'stance');
#nb_results(df, 'category');

print('\t\tREMOVING NOT ENOUGH CONTEXT');
df_no_NEC = df.loc[df.category != '4']
svm_results(df_no_NEC, 'category',True);
#nb_results(df_no_NEC, 'category',True);


'''
TO DO

iteratively
use 1-9 as training and only test on 1
use 1-8 as training and only test on 2
use 1-7 as training and only test on 3
'''
