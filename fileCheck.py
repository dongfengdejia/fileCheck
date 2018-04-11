#!/usr/bin/python


import os
import pprint
import subprocess
import sys
import commands

fileList = []
rootPath = os.getcwd();
rootPath = os.path.join(os.getcwd(), "..")
global storeFilePath

def filter(fullPath):
    if (fullPath == storeFilePath):
        return True
    elif (os.path.splitext(fullPath)[1] == ".js") or \
       (os.path.splitext(fullPath)[1] == ".json") or \
       (os.path.splitext(fullPath)[1] == ".py") or \
       (os.path.splitext(fullPath)[1] == ".txt") or \
       (os.path.splitext(fullPath)[1] == ".md"):
        return False
    else:
        return True
    
def getFileList(basePath):
    contentList = os.listdir(basePath);
    for content in contentList:
        fullPath = os.path.join(basePath, content)
        if os.path.isdir(fullPath):
            getFileList(fullPath)
        else:
            if filter(fullPath):
                continue
            fileList.append(fullPath)
            
def createStoreFile(): # True -> inited, False -> not inited
    if os.path.exists(storeFilePath):
        return True, open(storeFilePath,'r')
    else:
        return False, open(storeFilePath,'w')
    
def calcCheckSum(fileList):
    fileMap = {}
    for file in fileList:
        cmd = "sha256sum " + file
        output = commands.getoutput(cmd)
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        [checkSum, file] = output.stdout.read().split()
        fileMap[file] = checkSum
    return fileMap;
        
def saveStore(fileMap):
    storeFile = open(storeFilePath,'w')
    for key in fileMap:
        storeFile.writelines(key + " " + fileMap[key] + "\n")
    storeFile.close()
    print ">>> create storeFile: " + storeFilePath
    
def readCheckSum():
    fileMap = {}
    storeFile = open(storeFilePath,'r')
    for line in storeFile.readlines():
        [file, chechSum] = line.split()
        fileMap[file] = chechSum
    storeFile.close()
    return fileMap
    
def compleCheckSum(oldFileMap, newFileMap):
    for fileName in newFileMap:
        if oldFileMap.has_key(fileName):
            if newFileMap[fileName] != oldFileMap[fileName]:
                print "+++:" + fileName + " is changed"
        else:
            print "+++:" + fileName + " is new"
    
if __name__ == "__main__":

    if (len(sys.argv) > 1):
        if os.path.exists(sys.argv[1]):
            rootPath = sys.argv[1]
        else:
            print ">>> the root path not exist:", sys.argv[1]
            sys.exit(1)
    print ">>> file check root path:", rootPath
    storeFilePath = os.path.join(rootPath, "hashStorage.txt")
    print ">>> hash storage file:", storeFilePath
    getFileList(rootPath)
    
    isInit, checkSumStore = createStoreFile();
    if not isInit:
        fileMap = calcCheckSum(fileList)
        saveStore(fileMap)
    else:
        oldFileMap = readCheckSum()
        newFileMap = calcCheckSum(fileList)
        compleCheckSum(oldFileMap, newFileMap)
        
        
        