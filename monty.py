__author__ = 'lothilius'

import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import sys

#ABC_Glass_center.Spe
#Set apropriate directory depending on where I am working from.
inputFileDer = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/Lower_amp/"
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
    for i in range(12,16394):
        element = data[i][0].lstrip()
        newData.append(element)
    print type(newData)

    newData = np.array(newData)
    print type(newData)
    return newData

#plot data
def plotevents(datalist):
    x = range(0, len(datalist))
    x = np.array(x)

    #Make the plot
    axScatter = plt.subplot(111)
    axScatter.scatter(x, datalist)
    axScatter.set_aspect(1.)

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    #create the axes
    divider = make_axes_locatable(axScatter)
    axHistx = divider.append_axes("top", 1.2, pad=0.1, sharex=axScatter)

    # now determine nice limits by hand:
    binwidth = 0.25

    xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(datalist))])
    lim = ( int(xymax/binwidth) + 1) * binwidth
    bins = np.arange(-lim, lim + binwidth, binwidth)
    axHistx.hist(datalist, bins=bins)

    #axHistx.axis["bottom"].major_ticklabels.set_visible(False)
    for tl in axHistx.get_xticklabels():
        tl.set_visible(False)
    axHistx.set_yticks([0, 50, 100])

    #axHisty.axis["left"].major_ticklabels.set_visible(False)
    for tl in axHisty.get_yticklabels():
        tl.set_visible(False)
    axHisty.set_xticks([0, 50, 100])

    plt.draw()
    plt.show()


def main():
    fileName = raw_input("Type in file name: ")
    print(fileName)
    data = arrayFromFile(inputFileDer + fileName)
    data = cleanData(data)

    plotevents(data)

    return "done"


main()
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