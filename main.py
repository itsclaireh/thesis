#My Functions
from DataFrameImputer import *;
from clean import clean_tweet;
from compare import compare_and_load_datasets, remove_NEC, load_file;
from svm import svm_results, svm_results_stance, svm_results_related, svm_results_category_noNEC;
from naivebayes import nb_results_category, nb_results_category_noNEC;

import pandas as pd

file1 = 'MeTooMen.csv';
file2 = 'MeTooWomen.csv';
d = compare_and_load_datasets(file1, file2);

suppcat = load_file('supp_category.csv');
#suppstance = load_file('supp_stance.csv');
#supprel = load_file('supp_related.csv');

df=pd.concat([d,suppcat]);
#print(df);

#df = df.dropna();
#clean tweets
for i, row in df.iterrows():
  if row.text:
      df.set_value(i, 'text', clean_tweet(row.text));
      #df.iloc[i,df.columns.get_loc('text')]=clean_tweet(row.text);

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


print('\n');


svm_results(df, 'related');
svm_results(df, 'stance');
svm_results(df, 'category');



nb_results_category(df);


#df_no_NEC = df.loc[df.category != '4']
#df_no_NEC = remove_NEC(df);
#print(len(df_no_NEC.groupby(by='category')))
#svm_results_category_noNEC(df_no_NEC);

#nb_results_category_noNEC(df_no_NEC);
