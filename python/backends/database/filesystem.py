import os
import json

def loadDbDirectory(dirname):
    '''Load a full multiple series directory structure as described in the README'''
    series = []
    for subdir in os.listdir(dirname):
        if not os.path.isdir(subdir):
            continue
        else:
            series += loadDbDirectory(os.path.join(dirname, subdir))

def loadSeriesDirectory(dirname):
    '''Load a single single directory containing an info.json as described in the README'''
    
    infoFile   = os.path.join(dirname, "info.json")
    with open(infoFile) as f:
        return series.Series(json.load(f))
        
