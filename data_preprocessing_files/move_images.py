import os
import random
import shutil

files_list = []

for root, dirs, files in os.walk("train_images"):
    for file in files:
        #all 
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            files_list.append(os.path.join(root, file))


#print images
#lets me count and print the amount of jpeg,jpg,pmg 
file_count = len(files_list) 
print(file_count)

x = file_count // 20 # Move 5% of files from train to test

# print files_list   
filesToCopy = random.sample(files_list, x)  #prints x random files from list 

destPath = "test_images"

# if destination dir does not exists, create it
if os.path.isdir(destPath) == False:
        os.makedirs(destPath)

# iteraate over all random files and move them
for file in filesToCopy:
    shutil.move(file, destPath)