import os, time

path = os.getcwd()
list_files = os.listdir(path)

for file in list_files:
    if file.find("[EgyBest].") >= 0 :
        new_name = file.replace("[EgyBest].","")
        os.rename(file, new_name)
    elif file.find("[EgyBest]") >= 0 :
        new_name = file.replace("[EgyBest]","")
        os.rename(file, new_name)
    elif file.find("EgyBest") >= 0 :
        new_name = file.replace("EgyBest","")
        os.rename(file, new_name)