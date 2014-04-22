__author__ = 'lothilius'

import csv
import sys


inputFileDer = "/Users/admin/Dropbox/School/Spring-2014/PHY-474/Labs/Positronium/data/Enclosed/Lower_amp/"
fileName = ""

class Dataimport:
    #Pull data from CSV file
    def arrayFromFile(self, filename):
        """Given an external file containing numbers,
                create an array from those numbers."""
        dataArray = []
        with open(filename, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                dataArray.append(row)
        spamreader.close()
        return dataArray


    def cleanData(data):
        """Once a file has been read and placed in list
            package the data so that it is useful"""
        newData = []
        for item in data:
            newData.append(item.lstrip())
        return newData

    def main(self):
        fileName = raw_input("Type in file name: ")
        print(fileName)
        data = self.arrayFromFile(inputFileDer + fileName)
        #data = cleanData(data)
        for each in data:
            print(each)
            print('\n')
        return "done"



while True:
    get_data = Dataimport()
    try:
        get_data.main()
    except:
        print get_data.main()
    print "\n\nWould you like to start another capture" \
          + " session? (Y/N)"
    Doagain = str(raw_input(""))
    if ('Y' not in Doagain) and ('y' not in Doagain):
        print "Good Bye!"
        break