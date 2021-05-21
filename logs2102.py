#!/bin/bash/python3
#-------------------------------------------
# Program by Mikhail L.
#
#Version     Date     
#1.0         2021
#
#-------------------------------------------
import shutil 
import os 
import sys 

#---------------------------------------------------------------
#  logs2102.py       mylog.txt      10          5              /
#  script itself     source file   size   how many copies     /
#-------------------------------------------------------------
if(len(sys.argv) < 4):
    print("Mising arguments! Usage format is : script.py 10  5 ")
    exit(1)

file_name = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size
    logfile_size  = logfile_size / 1024 

    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum-1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src,dst)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + "   to " + file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()