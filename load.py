import csv
import numpy as np
import urllib.request

with urllib.request.urlopen("https://raw.githubusercontent.com/claireballoon/thesis/master/TestData.tsv") as url:
    raw_data = url.read().decode('utf-8')

dataset = np.loadtxt(raw_data, delimiter="\t")
X = dataset[:,0:1]
y = dataset[:,2]

names=['id_str','text','relevant']
categories=['1','2']

print(names)
print(dataset)
