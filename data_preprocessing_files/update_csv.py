from attr import field
import pandas as pd
import os
import random
import shutil


all_data = pd.read_csv('./all_data.csv',index_col='image')

# Convert to dictionary because pandas got issue recognizing values
dic = all_data.to_dict()
dic = dic['labels']

# find all files in the test directory
from os import listdir
from os.path import isfile, join
mypath = './test_images'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

test_dic = {}
for file in onlyfiles:
    test_dic[file] = dic[file] # assign the value in the original dictionary to the test dictionary
    dic.pop(file,None) # remove the file in dictionary

train_dic = dic # Assign the name for consistency


# convert dictionaries to csv files
import csv
# Write train.csv
with open('train.csv','w',newline='') as csvfile:
    fieldnames = ['image','labels']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    for key in train_dic:
        writer.writerow({'image': key, 'labels': train_dic[key]})

with open('test.csv','w',newline='') as csvfile:
    fieldnames = ['image','labels']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    for key in test_dic:
        writer.writerow({'image': key, 'labels': test_dic[key]})