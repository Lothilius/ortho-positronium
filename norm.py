__author__ = 'martin'

from monty import arrayFromFile
from monty import cleanData
from monty import plotevents
import csv
import numpy as np
import os



def normlize(data_small, data_large, binnum):
    """Normalizes the data of the larger count data_large
    :rtype : numpy array
    according to the count rate of data_small"""
    data_small = np.array(data_small)
    data_large = np.array(data_large)

    newlist = np.divide(data_small, data_large[binnum])
    finlist = np.multiply(newlist, data_large)
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
            inputFileDer = "/Users/martin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/HV_Failure/"
            outputfiledir = "/Users/martin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/play_data/"
        elif file is 'admin':
            inputFileDer = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/HV_Failure/"
            outputfiledir = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/play_data/"


    file1 = arrayFromFile(inputFileDer + 'ACal_5.Spe') #raw_input("Type in file name: ")
    file2 = "BCal_5.Spe"  #raw_input("Type in file name: ")
    file3 = arrayFromFile(inputFileDer + 'CCal_3.Spe')
    file1 = cleanData(file1)
    file3 = cleanData(file3)

    normdata = norm(file1, file3)
    print(len(normdata))
    arrayTofile(normdata, outputfiledir + 'CNorm_2')
    #plotevents(data)

    return "done"



main()

