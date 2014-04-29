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


#Extract data from the list made from reading the file
def cleanData(data):
    """Once a file has been read and placed in list,
        package the data so that it is useful"""
    newData = []
    for i in range(12, 524):
        element = int(data[i][0].lstrip())
        newData.append(element)

    #newData = np.array(newData)
    return newData


#plot data
def plotevents(datalist):
    x = range(0, len(datalist))
    x = np.array(x)
    y = datalist

    #plt.plot(x,y, linestyle=None)
    #fig, ax = plt.subplots()
    plt.scatter(x,y,s=20, marker='.', c='blue')

    plt.show()
    return "done"

#Combine the data of two runs in a monte carlo manor
def combine(run1, run2, run3, inputFileDer):
    """Combines the two sets of data for the files entered
    at the beginning of the program"""
    data1 = arrayFromFile(inputFileDer + run1)
    data1 = cleanData(data1)
    plotevents(data1)

    data2 = arrayFromFile(inputFileDer + run2)
    data2 = cleanData(data2)

    prob1 = getprob(data1)
    prob2 = getprob(data2)

    if run3 is not 0:
        data3 = arrayFromFile(inputFileDer + run3)
        data3 = cleanData(data3)

        prob3 = getprob(data3)

    createcounts(prob1, prob2, prob3)

#Create a range of randum numbers.
def rndnumbers(binrng, totcounts):
    numbers = []
    for i in range(0, totcounts):
         numbers.append(np.random.random_integers(binrng-1))
    return numbers

#Given lists of counts for each bin spit out the coincidence plot
def createcounts(prob1, prob2, prob3):
    coin = [0] * 16383
    counts1 = []
    counts2 = []
    counts3 = []

    #Create three lists of 10000 random numbers
    number1 = rndnumbers(len(prob1), 10000000)
    number2 = rndnumbers(len(prob2), 10000000)
    number3 = rndnumbers(len(prob3), 10000000)
    print(len(prob1), len(prob2), len(prob3))

    for item in number1:
        binnum = prob1[item]
        counts1.append(binnum)

    for item in number2:
        binnum = prob2[item]
        counts2.append(binnum)

    for item in number3:
        binnum = prob3[item]
        counts3.append(binnum)


    for i in range(len(counts3)):
        binnum = counts1[i] + counts2[i] + counts3[i]
        if binnum < len(coin):
            coin[binnum] += 1

    print(len(coin))

    #for item in binnum:

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


def main():
    file1 = "ACal_2.Spe" #raw_input("Type in file name: ")
    file2 = "BCal_2.Spe" #raw_input("Type in file name: ")
    file3 = "CCal_2.Spe"

    combine(file1, file2, file3)

    #plotevents(data)

    return "done"



main()
def commentout():
    while True:
        try:
            request = input("Would you like to plot, or create a coincidence?")
            if request is "plot":
                file = input("Please enter full directory and file name: ")

            main()
        except:
            print "error"
        print "\n\nWould you like to start another capture" \
              + " session? (Y/N)"
        Doagain = str(raw_input(""))
        if ('Y' not in Doagain) and ('y' not in Doagain):
            print "Good Bye!"
            break