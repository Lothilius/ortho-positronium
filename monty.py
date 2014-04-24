__author__ = 'lothilius'

import csv
import os
import numpy as np
import matplotlib.pyplot as plt


#ABC_Glass_center.Spe
#Set apropriate directory depending on where I am working from.
inputFileDer = "/Users/martin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/Lower_amp/"
directory = []
for file in os.listdir("/Users/"):
    if file is "admin":
        print file
        inputFileDer = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/Lower_amp/"

fileName = ""

#Pull data from CSV file
def arrayFromFile(filename):
    """Given an external file containing numbers,
            create an array from those numbers."""
    dataArray = []
    with open(filename, 'r+') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            dataArray.append(row)
    return dataArray


#Extract data from the list made from reading the file
def cleanData(data):
    """Once a file has been read and placed in list
        package the data so that it is useful"""
    newData = []
    for i in range(12, 16394):
        element = int(data[i][0].lstrip())
        newData.append(element)

    #newData = np.array(newData)
    return newData


#plot data
def plotevents(datalist):
    x = range(0, len(datalist))
    x = np.array(x)
    y = datalist

    plt.plot(x,y)
    #fig, ax = plt.subplots()
    plt.scatter(x,y, marker=".")

    plt.draw()
    plt.show()
    return "done"

#Combine the data of two runs in a monte carlo manor
def combine(run1, run2):
    """Combines the two sets of data for the files entered
    at the beginning of the program"""
    data1 = arrayFromFile(inputFileDer + run1)
    data1 = cleanData(data1)

    data2 = arrayFromFile(inputFileDer + run1)
    data2 = cleanData(data2)

    prob1 = getprob(data1)
    prob2 = getprob(data2)

    createcounts(prob1, prob2)

#Create a range of randum numbers.
def rndnumbers(binrng, totcounts):
    numbers = []
    for i in range(0, totcounts):
         numbers.append(np.random.random_integers(binrng))

    return numbers

#given lists of counts for each bin spit out the coincidence plot
def createcounts(prob1, prob2):
    coin = [0] * 16382

    number1 = rndnumbers(len(prob1), 10000)
    number2 = rndnumbers(len(prob2), 10000)

    for item in number1:
        binnum = prob1[item]
        coin[binnum] += 1

    for item in number2:
        binnum = prob2[item]
        coin[binnum] += 1

    plotevents(coin)





#Create a probability array with the number of events in a bin is the number of occurances in the array for the bin.
#Items in array are bin numbers.
def getprob(data):
    problist = []

    for i, item in enumerate(data):
        while (item is not 0):
           problist.append(i)
           item -= 1


    return problist


#"/Users/martin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/Lower_amp/"

def main():
    request = str(raw_input("Would you like to plot, or create a coincidence? "))
    if 'plot' in request:
        thefile = str(raw_input("Please enter full directory and file name: "))
        data1 = arrayFromFile(thefile)
        data1 = cleanData(data1)
        plotevents(data1)
    elif "coin" in request:
        filesnum = str(raw_input("How many coincidence files are there 2 or 3? "))
        inputFileDer = str(raw_input("Please enter path to files: "))
        if filesnum is 2:
            file1 = inputFileDer + str(raw_input("Type in 1st file name: ")) #"ACal_2.Spe"
            file2 = inputFileDer + str(raw_input("Type in 2nd file name: ")) #"BCal_2.Spe"

            combine(file1,file2)

        elif filesnum is 3:
            file1 = raw_input("Type in 1st file name: ") #"ACal_2.Spe"
            file2 = raw_input("Type in 2nd file name: ") #"BCal_2.Spe"
            file3 = raw_input("Type in 3rd file name: ") #"CCal_2.Spe"

            combine(file1,file2)
            print("done")
            #plotevents(data)
        else:
            ValueError

    else:
        ValueError


while True:
    try:
        main()
    except:
        print "error"
    print "\n\nWould you like to start another capture" \
          + " session? (Y/N)"
    Doagain = str(raw_input(""))
    if ('Y' not in Doagain) and ('y' not in Doagain):
        print "Good Bye!"
        break