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
    binnum = 221
    data1 = arrayFromFile(inputFileDer + run1)
    data2 = arrayFromFile(inputFileDer + run2)


    data1 = cleanData(data1)
    data2 = cleanData(data2)
    #Normalize data according to the lower vallue in bin number binnum
    if data1[binnum] < data2[binnum]:
        data2 = normlize(data1, data2, binnum)
    else:
        data1 = normlize(data2, data1, binnum)

    if run3 != 0:
        data3 = arrayFromFile(inputFileDer + run3)
        data3 = cleanData(data3)

        if data1[binnum] < data3[binnum]:
            data3 = normlize(data1, data3, binnum)
        else:
            data1 = normlize(data3, data1, binnum)
            data2 = normlize(data3, data2, binnum)

        prob1 = getprob(data1)
        prob2 = getprob(data2)
        prob3 = getprob(data3)
    else:
        prob1 = getprob(data1)
        prob2 = getprob(data2)

    bincount = []
    for each in range(1, 100):
        simcounts = createcounts(prob1, prob2, prob3)
        bincount.append(simcounts[221])
        if each == 1:
            filename = inputFileDer + 'simulationS'
            arrayTofile(simcounts, filename)


    filename = inputFileDer + "countS"
    arrayTofile(bincount, filename)

#write an array to a file.
def arrayTofile(dataArray, fileNum):
    fileName = fileNum + "_a.csv"
    print(fileName)
    with open(fileName, 'w+') as csvfile:
        linewriter = csv.writer(csvfile, delimiter= ",")
        for each in dataArray:
            linewriter.writerow([each])
    print("done")


#Create2jksrange of randum numbers.
def rndnumbers(binrng, totcounts):
    numbers = []
    for i in range(0, totcounts):
         numbers.append(np.random.random_integers(binrng-1))
    return numbers

#Given lists of counts for each bin spit out the coincidence plot
def createcounts(prob1, prob2, prob3):
    coin = [0] * 512
    counts1 = []
    counts2 = []
    counts3 = []

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


    for i in range(len(counts1)):
        binnum = counts1[i] + counts2[i] + counts3[i]
        if binnum < len(coin):
            coin[binnum] += 1

    return(coin)

    #for item in binnum:



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
    #Set apropriate directory depending on where I am working from.
    for file in os.listdir("/Users/"):
        if file == 'martin':
            print("Welcome Martin")
            inputFileDer = "/Users/martin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/HV_Failure/"
            break
        elif file == 'admin':
            print("Welcome Admin")
            inputFileDer = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/HV_Failure/"
            break

    file1 = "ACal_5.Spe" #raw_input("Type in file name: ")
    file2 = "BCal_5.Spe" #raw_input("Type in file name: ")
    file3 = "CCal_5.Spe"

    combine(file1, file2, file3, inputFileDer)

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