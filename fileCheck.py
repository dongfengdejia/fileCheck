#!/usr/bin/python


import os
import pprint
import subprocess

fileList = []
rootPath = os.getcwd();
rootPath = os.path.join(os.getcwd(), "..")
storeFilePath = os.path.join(rootPath, "checkSum.txt")

def filter(fullPath):
    if fullPath == storeFilePath:
        return True;
    return False;
    
def getFileList(basePath):
    contentList = os.listdir(basePath);
    for content in contentList:
        fullPath = os.path.join(basePath, content)
        if filter(fullPath):
            continue
        if os.path.isdir(fullPath):
            getFileList(fullPath)
        else:
            fileList.append(fullPath)
            
def createStoreFile(): # True -> inited, False -> not inited
    if os.path.exists(storeFilePath):
        return True, open(storeFilePath,'r')
    else:
        return False, open(storeFilePath,'w')
    
def calcCheckSum(fileList):
    fileMap = {}
    for file in fileList:
        cmd = "sha256sum " + file + "\r\n"
        output = subprocess.check_output(cmd)
        [chechSum, file] = output.split()
        fileMap[file] = chechSum
    return fileMap;
        
def saveStore(fileMap):
    storeFile = open(storeFilePath,'w')
    for key in fileMap:
        storeFile.writelines(key + " " + fileMap[key] + "\n")
    storeFile.close()
    print "create storeFile: " + storeFilePath
    
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
                print fileName + " is changed"
        else:
            print fileName + " is new"
    
if __name__ == "__main__":
    getFileList(rootPath);
    isInit, checkSumStore = createStoreFile();
    if not isInit:
        fileMap = calcCheckSum(fileList)
        saveStore(fileMap)
    else:
        oldFileMap = readCheckSum()
        newFileMap = calcCheckSum(fileList)
        compleCheckSum(oldFileMap, newFileMap)
        
        
        