import csv
import numpy as np
import urllib.request
import scipy
import pandas
from io import StringIO
from sklearn.preprocessing import MinMaxScaler

url = "https://raw.githubusercontent.com/claireballoon/thesis/master/TestData.tsv"
names=['id_str','text','relevant']
dataframe = pandas.read_csv(url, sep='/t',engine='python')

dataframe.shape


#array = dataframe.values

#print(array)

#with urllib.request.urlopen("https://raw.githubusercontent.com/claireballoon/thesis/master/TestData.tsv") as url:
#    raw_data = url.read().decode('utf-8')

#dataset = np.loadtxt(raw_data, delimiter="\t")
#X = dataset[:,0:1]
#y = dataset[:,2]


#categories=['1','2']

#print(names)
#print(dataset)
