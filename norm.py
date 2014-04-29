__author__ = 'martin'

from monty import arrayFromFile
from monty import cleanData
from monty import plotevents
import csv
import numpy as np
import os



def norm(dataarray1, dataarray2):
    dataarray1 = np.array(dataarray1)
    dataarray2 = np.array(dataarray2)

    newlist = np.subtract(dataarray2, dataarray1)
    newlist = np.divide(newlist, dataarray2)
    newlist = np.subtract(1, newlist)
    finlist = np.multiply(newlist, dataarray2)
    return finlist

#write an array to a file.
def arrayTofile(dataArray, fileNum):
    fileName = fileNum+"_a.csv"
    print(fileName)
    with open(fileName, 'w+') as csvfile:
        linewriter = csv.writer(csvfile, delimiter= ",")
        for each in dataArray:
            linewriter.writerow([each])
    print("done")


def main():
    for file in os.listdir("/Users/"):
        if file == "martin":
            inputFileDer = "/Users/martin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/Lower_amp/"
            outputfiledir = "/Users/martin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/play_data/"
        elif file is 'admin':
            inputFileDer = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/Lower_amp/"
            outputfiledir = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/play_data/"


    file1 = arrayFromFile(inputFileDer + 'ACal_3.Spe') #raw_input("Type in file name: ")
    file2 = "BCal_2.Spe" #raw_input("Type in file name: ")
    file3 = arrayFromFile(inputFileDer + 'CCal_3.Spe')
    file1 = cleanData(file1)
    file3 = cleanData(file3)

    normdata = norm(file1, file3)
    print(len(normdata))
    arrayTofile(normdata, outputfiledir + 'CNorm_2')
    #plotevents(data)

    return "done"



main()

