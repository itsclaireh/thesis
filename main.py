#My Functions
from DataFrameImputer import *;
from clean import clean_tweet;
from compare import compare_and_load_datasets, remove_NEC;
from svm import svm_results_category, svm_results_stance, svm_results_related, svm_results_category_noNEC;

file1 = 'MeTooMen.csv';
file2 = 'MeTooWomen.csv';
df = compare_and_load_datasets(file1, file2);

#df = df.dropna();
#clean tweets
for i, row in df.iterrows():
  if row.text:
      df.set_value(i, 'text', clean_tweet(row.text));

print(df);

print('\nPRINTING RESULTS:');

svm_results_related(df);
svm_results_stance(df);
svm_results_category(df);

df_no_NEC = remove_NEC(df);

svm_results_category_noNEC(df_no_NEC);
