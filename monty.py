__author__ = 'lothilius'

import csv
import os
import numpy as np
import matplotlib.pyplot as plt


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

def normlize(data_small, data_large, binnum):
    """Normalizes the data of the larger count data_large
    :rtype : numpy array
    according to the count rate of data_small"""

    #data_small = np.array(data_small)
    #data_large = np.array(data_large)

    percent = data_small[binnum] / float(data_large[binnum])
    finlist = []
    for each in data_large:
        num = round(each * percent, 0)
        finlist.append(int(num))
    return finlist

#Extract data from the list made from reading the file
def cleanData(data):
    """Once a file has been read and placed in list
        package the data so that it is useful

    Returns array with data from bins 12 through 16394
    """
    newData = []
    for i in range(12, 524):
        element = int(data[i][0].lstrip())
        newData.append(element)

    #newData = np.array(newData)
    return newData


def plotevents(datalist):
    """Plot data

    Returns string done
    """
    x = range(0, len(datalist))
    x = np.array(x)
    y = datalist

    #plt.plot(x,y, linestyle=None)
    #fig, ax = plt.subplots()
    plt.scatter(x,y,s=20, marker='.', c='blue')

    plt.show()
    return "done"


def combine(run1, run2):
    """Combines the two sets of data for the files entered
    at the beginning of the program

    Return none
    """
    data1 = arrayFromFile(run1)
    data1 = cleanData(data1)

    data2 = arrayFromFile(run2)
    data2 = cleanData(data2)


    createcounts(prob1, prob2)


def rndnumbers(binrng, totcounts):
    """Create a range of random numbers.

    Return array of random numbers
    """
    numbers = []
    for i in range(0, totcounts):
         numbers.append(np.random.random_integers(binrng-1))
    return numbers


def createcounts(prob1, prob2):
    """Given lists of counts for each bin spit out the coincidence plot

    Return none
    """
    coin = [0] * 16382

    #Create three lists of 10000 random numbers
    number1 = rndnumbers(len(prob1), 500027)
    number2 = rndnumbers(len(prob2), 500027)
    number3 = rndnumbers(len(prob3), 500027)

    for item in number1:
        binnum = prob1[item]
        counts1.append(binnum)

    for item in number2:
        binnum = prob2[item]
        counts2.append(binnum)

    for item in number3:
        binnum = prob3[item]
        counts3.append(binnum)


def getprob(data):
    """Create a probability array with the number of events in a bin is the number of occurrences in the array
    for the bin.Items in array are bin numbers.

    Return array containing bin numbers that occurred.
    """
    problist = []

    for i, item in enumerate(data):
        while (item is not 0):
           problist.append(i)
           item -= 1


    return problist


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
        if filesnum == '2':
            file1 = inputFileDer + str(raw_input("Type in 1st file name: ")) #"ACal_2.Spe"
            file2 = inputFileDer + str(raw_input("Type in 2nd file name: ")) #"BCal_2.Spe"

            combine(file1, file2)

        elif filesnum == '3':
            file1 = raw_input("Type in 1st file name: ") #"ACal_2.Spe"
            file2 = raw_input("Type in 2nd file name: ") #"BCal_2.Spe"
            file3 = raw_input("Type in 3rd file name: ") #"CCal_2.Spe"

            combine(file1, file2)
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
    print "\n\nWould you like to start another session? (Y/N)"
    Doagain = str(raw_input(""))
    if ('Y' not in Doagain) and ('y' not in Doagain):
        print "Good Bye!"
        break
