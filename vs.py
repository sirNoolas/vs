#!/usr/bin/python3.4

# The MIT License (MIT)
# 
# Copyright (c) 2015 David
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import time

def getStartInput():
    # init variables
    release = 0
    major = 0
    minor = 0
    bugs = 0
    
    # if the user already has a version for its program, use that.
    print("Use custom start version? (default is 0.0.0.0)(y/n)")
    userInput = input().lower()
    while (userInput.startswith('h')):
        tellCommands()
        userInput = input().lower()
    if (userInput.startswith("y")):
        print("Current version (Release.major.minor.bugfix):")
        release = getInt("release: ")
        major = getInt("major: ")
        minor = getInt("minor: ")
        bugs = getInt("bugfixes/builds: ")

        vString = str(release) + "." + str(major) + "." + str(minor) + "." + str(bugs)
        print("The version which will be used from now on is:" + vString)
    else:
        print("default version is used")


    fv = str(release) + "." + str(major) + "." + str(minor) + "." + str(bugs)
    timestamp = time.strftime("%d/%m/%Y %X")
    with open('./history.vs', 'a') as file:
        file.write(fv + " @ " + timestamp + "\n")
    with open('./current.vs', 'w') as file:
        file.write(fv)
        
    return [release, major, minor, bugs]

def loadStartValues():
    version = ""
    with open('./current.vs', 'r') as file:
        version = file.readline().split('.')

    # if no version can be read from the file, don't even bother to ask the user
    if (version[0] != ""):
        # Convert list of strings to list of integers:
        for i in range(0,4):
            version[i] = int(version[i])
            
        print("Load previous version? (y/n)")
        userInput = input().lower()
        while (userInput.startswith('h')):
            tellCommands()
            userInput = input().lower()
        if (userInput.startswith("y")):
            return version
    return getStartInput()

def getInt(message):
    # get an integer from the user; displays message before asking input
    x = 0
    while True:
        try:
            x = int(input(message))
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            break
    return x

def tellCommands():
    print("The following commands can only be used when a version has been initialised:")
    print("'release'/'major'/'minor'/'bug' - increase given version entry")
    print("'history' - display the version history")
    print("'reset'   - delete version history and start with version 0.0.0.0")
    print("'exit'    - exit the program and store current version")

def doInput(curVer):
    print("current version: " + str(curVer[0]) + "." + str(curVer[1]) + "." + str(curVer[2]) + "." + str(curVer[3]))
    uIn = input("Command: ").lower()
    if (uIn == "exit"):
        return uIn
    elif (uIn == "reset"):
        with open('./current.vs', 'w') as file:
            file.write("")
        with open('./history.vs', 'w') as file:
            file.write("")
        return uIn
    elif (uIn == "history"):
        with open('history.vs', 'r') as file:
            print(file.read()) # this may cause memory overflow
    elif (uIn == "release"):
        curVer[0] += 1
        store()
    elif (uIn == "major"):
        curVer[1] += 1
        store()
    elif (uIn == "minor"):
        curVer[2] += 1
        store()
    elif (uIn == "bug"):
        curVer[3] += 1
        store()
    elif (uIn.startswith('h')):
        tellCommands()
    else:
        print("Please enter a valid command!\nEnter 'h' for help")
    return "continue"

def checkFiles():
    with open('history.vs', 'a+') as file:
        line = file.readline()
        #if (line != ""): #awesome
    with open('./current.vs', 'w+') as file:
        line = file.readline()
        #if (line != ""): #awesome

def store():
    fv = str(version[0]) + "." + str(version[1]) + "." + str(version[2]) + "." + str(version[3])
    timestamp = time.strftime("%d/%m/%Y %X")
    with open('./history.vs', 'a') as file:
        file.write(fv + " @ " + timestamp + "\n")
    with open('./current.vs', 'w') as file:
        file.write(fv)
        
#
# end of functions; start of main
# =====================================================================

print("This is the auto versioner made by sirNoolas")
print("Versions are given as: (Release.major.minor.bugfix) ")
print("v:0.3\n")
print("type 'h' or 'help' for a list of possible commands")

#checkFiles() # If history.vs and current.vs don't excist, create them
version = loadStartValues() #[0, 0, 0, 0] == [Release, major, minor, bugfix]

status = "start"
while status != "exit":
    status = doInput(version)                      
    if (status == "reset"):
        version = loadStartValues()

sys.exit(0)
        
    

