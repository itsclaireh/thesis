import pandas as pd

#load a file
def load_file(filename):

    df = pd.read_csv(filename,header=None,index_col=None,encoding='latin1',dtype='str');
    df.columns=['id_str','text','related','stance','category'];
    return df;

#compare two identical files
#take only the responses that agree
def compare_and_load_datasets(file1, file2):

    dfmen = load_file(file1);
    dfwomen = load_file(file2);

    #create the df to return
    #we want anything else to be NaN
    ix=range(0,len(dfmen));
    col=['id_str','text','related','stance','category'];
    df = pd.DataFrame(index=ix,columns=col);

    for index, row in dfwomen.iterrows():
        #ensure tweet IDs are identical
        if dfmen.iloc[[index]].id_str.values[0] == dfwomen.iloc[[index]].id_str.values[0]:
            df.at[index,'id_str'] = row.id_str;
            #some of them are weird, let's make sure the text is identical too
            if dfmen.iloc[[index]].text.values[0] == dfwomen.iloc[[index]].text.values[0]:
                df.at[index,'text'] = row.text;
                #check to make sure it's a number and not NaN
                #we only need to check the row (in dfwomen) because if they're not
                #the same we don't care anyway
                if row.related == '1' or row.related=='2':
                    #are the "related" answers the same
                    if str(dfmen.iloc[[index]].related.values[0]) == str(dfwomen.iloc[[index]].related.values[0]):
                        #if so, fill in df with the shared answer
                        #if not, leave as NaN
                        df.at[index,'related'] = row.related;
                #check to make sure it's a number and not NaN
                if row.stance == '1' or row.stance=='2' or row.stance=='3':
                    if str(dfmen.iloc[[index]].stance.values[0]) == str(dfwomen.iloc[[index]].stance.values[0]):
                        df.at[index,'stance'] = row.stance;
                #check to make sure it's a number and not NaN
                if row.category == '1' or row.category=='2' or row.category=='3' or row.category=='4':
                    if str(dfmen.iloc[[index]].category.values[0]) == str(dfwomen.iloc[[index]].category.values[0]):
                        df.at[index,'category'] = row.category;

    #drop the row if every value is NaN because we didn't gain anything from that)
    #we still care if it's something like 1/1/NaN so ignore those for now
    #thresh 3 means keep rows with at least 3 non-NaN values (id, text, and at least 1 other)
    df = df.dropna(axis=0, thresh=3);
    return(df);

#this was for removing the Not Enough Context Category, which wasn't actually helpful in the end
def remove_NEC(dfOld):
    ix=range(0,len(dfOld));
    col=['id_str','text','related','stance','category'];
    df = pd.DataFrame(index=ix,columns=col);

    for index, row in df.iterrows():
        if row.category == '1' or row.category=='2' or row.category=='3':
            df.at[index,'category'] = row.category;

    df = df.dropna(axis=0, thresh=3);
    return df;
