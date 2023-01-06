import os
import json
import python.series as series
import sys

def loadDbDirectory(enforce, dirname):
    '''Load a full multiple series directory structure as described in the README'''

    series = []
    for sub in os.listdir(dirname):
        fullpath = os.path.join(dirname, sub)

        if sub == ".git":
            continue
        elif not os.path.isdir(fullpath):
            continue
        else:
            series += [ loadSeriesDirectory(enforce, fullpath) ]
    
    return sorted(series, reverse=True)

def loadSeriesDirectory(enforce, dirname):
    '''Load a single single directory containing an info.json as described in the README'''

    infoFile   = os.path.join(dirname, "info.json")
    with open(infoFile) as f:
        try:
            data = json.load(f)
            return series.Series(data, enforceComplete=enforce)
        except json.decoder.JSONDecodeError as e:
            print("Failed to decode {} - {}".format(infoFile, e))
            sys.exit(1)

def loadUserDirectory(dirname):
    ''''Load a single directory containing all ratings of a given user'''

    for sub in os.listdir(dirname):
        fullpath = os.path.join(dirname, sub)
        filename = os.path.join(fullpath, "info.json")

