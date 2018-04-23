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
