#My Functions
from DataFrameImputer import *;
from clean import clean_tweet;
from compare import compare_and_load_datasets, remove_NEC, load_file;
from svm import svm_results;
from naivebayes import nb_results;
import pandas as pd

def reductionRel(df,percentage):
    return df.drop(df.query('related in ["1"]').sample(frac=percentage).index);

def reductionRelAll(df):
    print('Reduction by 10%...');
    df = reductionRel(df,.1);
    df_rel1 = df.loc[df.related=='1'];
    print('Relevant:\t{0}'.format(len(df_rel1)));
    svm_results(df,'related');

    print('Reduction by 20%...');
    df = reductionRel(df,.2);
    df_rel1 = df.loc[df.related=='1'];
    print('Relevant:\t{0}'.format(len(df_rel1)));
    svm_results(df,'related');

    print('Reduction by 25%...');
    df = reductionRel(df,.225);
    df_rel1 = df.loc[df.related=='1'];
    print('Relevant:\t{0}'.format(len(df_rel1)));
    svm_results(df,'related');

    print('Reduction by 2%...');
    df = reductionRel(df,.25);
    df_rel1 = df.loc[df.related=='1'];
    print('Relevant:\t{0}'.format(len(df_rel1)));
    svm_results(df,'related');

    print('Reduction by 30%...');
    df = reductionRel(df,.3);
    df_rel1 = df.loc[df.related=='1'];
    print('Relevant:\t{0}'.format(len(df_rel1)));
    svm_results(df,'related');

    print('Reduction by 35%...');
    df = reductionRel(df,.35);
    df_rel1 = df.loc[df.related=='1'];
    print('Relevant:\t{0}'.format(len(df_rel1)));
    svm_results(df,'related');

    print('Reduction by 40%...');
    df = reductionRel(df,.4);
    df_rel1 = df.loc[df.related=='1'];
    print('Relevant:\t{0}'.format(len(df_rel1)));
    svm_results(df,'related');

def reductionCat(df,percentage):
    return df.drop(df.query('category in ["4"]').sample(frac=percentage).index);

def reductionCatAll(df):
    print('Reduction by 5%...');
    df = reductionCat(df,.05);
    df_NEC = df.loc[df.category=='4'];
    print('NEC:\t{0}'.format(len(df_NEC)));
    svm_results(df,'category');
    print('Reduction by 10%...');
    df = reductionCat(df,.1);
    df_NEC = df.loc[df.category=='4'];
    print('NEC:\t{0}'.format(len(df_NEC)));
    svm_results(df,'category');
    print('Reduction by 15%...');
    df = reductionCat(df,.15);
    df_NEC = df.loc[df.category=='4'];
    print('NEC:\t{0}'.format(len(df_NEC)));
    svm_results(df,'category');
    print('Reduction by 20%...');
    df = reductionCat(df,.2);
    df_NEC = df.loc[df.category=='4'];
    print('NEC:\t{0}'.format(len(df_NEC)));
    svm_results(df,'category');
    print('Reduction by 25%...');
    df = reductionCat(df,.25);
    df_NEC = df.loc[df.category=='4'];
    print('NEC:\t{0}'.format(len(df_NEC)));
    svm_results(df,'category');

def reductionStance(df,percentage):
    return df.drop(df.query('stance in ["1"]').sample(frac=percentage).index);

def reductionStanceAll(df):
    print('Reduction by 10%...');
    df = reductionStance(df,.1);
    newsize = df.loc[df.stance=='1'];
    print('NEC:\t{0}'.format(len(newsize)));
    svm_results(df,'stance');
    print('Reduction by 20%...');
    df = reductionStance(df,.2);
    newsize = df.loc[df.stance=='1'];
    print('NEC:\t{0}'.format(len(newsize)));
    svm_results(df,'stance');
    print('Reduction by 25%...');
    df = reductionStance(df,.25);
    newsize = df.loc[df.stance=='1'];
    print('NEC:\t{0}'.format(len(newsize)));
    svm_results(df,'stance');
    print('Reduction by 30%...');
    df = reductionStance(df,.3);
    newsize = df.loc[df.stance=='1'];
    print('NEC:\t{0}'.format(len(newsize)));
    svm_results(df,'stance');
    print('Reduction by 35%...');
    df = reductionStance(df,.35);
    newsize = df.loc[df.stance=='1'];
    print('NEC:\t{0}'.format(len(newsize)));
    svm_results(df,'stance');
    print('Reduction by 40%...');
    df = reductionStance(df,.4);
    newsize = df.loc[df.stance=='1'];
    print('NEC:\t{0}'.format(len(newsize)));
    svm_results(df,'stance');

file1 = 'data/MeTooMen.csv';
file2 = 'data/MeTooWomen.csv';
d = compare_and_load_datasets(file1, file2);

supp = load_file('data/supplemental.csv');
df=pd.concat([d,supp]);
#print(df);

supp2 = load_file('data/suppTweetsNoID.csv');
df=pd.concat([df,supp2]);

men = load_file(file1);
women = load_file(file2);


#clean tweets
for i, row in df.iterrows():
  if row.text:
      df.set_value(i, 'text', clean_tweet(row.text));
      men.set_value(i, 'text',clean_tweet(row.text));
      women.set_value(i, 'text',clean_tweet(row.text));
      #df.at[df.index[i-2], 'text'] = clean_tweet(row.text);

'''
print('\nPRINTING RESULTS WOMEN:');


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


print('\nPRINTING RESULTS MEN:');


men_cat1 = men.loc[df.category=='1'];
men_cat2 = men.loc[df.category=='2'];
men_cat3 = men.loc[df.category=='3'];
men_cat4 = men.loc[df.category=='4'];

print('\nTOTAlS:');
print('Patronizing:\t\t\t{0}'.format(len(men_cat1)));
print('Unwanted Sexual Attention:\t{0}'.format(len(men_cat2)));
print('Predatory:\t\t\t{0}'.format(len(men_cat3)));
print('Not Enough Context:\t\t{0}'.format(len(men_cat4)));

men_rel1 = men.loc[df.related=='1'];
men_rel2 = men.loc[df.related=='2'];
print('\nTOTAlS:');
print('Relevant:\t\t{0}'.format(len(men_rel1)));
print('Irrelevant:\t\t{0}'.format(len(men_rel2)));

men_st1 = men.loc[df.stance=='1'];
men_st2 = men.loc[df.stance=='2'];
men_st3 = men.loc[df.stance=='3'];
print('\nTOTAlS:');
print('Support:\t\t{0}'.format(len(men_st1)));
print('Against:\t\t{0}'.format(len(men_st2)));
print('Neutral:\t\t{0}'.format(len(men_st3)));
'''

print('\n');

svm_results(df, 'related');
dfnew = reductionRelAll(df);

svm_results(df,'category');
dfnew3 = reductionCatAll(df);

svm_results(df,'stance');
dfnew2 = reductionStanceAll(df);

#svm_results(df, 'stance');
#svm_results(df, 'category');

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
