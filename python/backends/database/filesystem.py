import os
import json
import python.series as series

def loadDbDirectory(dirname):
    '''Load a full multiple series directory structure as described in the README'''

    series = []
    for sub in os.listdir(dirname):
        fullpath = os.path.join(dirname, sub)

        if sub == ".git":
            continue
        elif not os.path.isdir(fullpath):
            continue
        else:
            series += [ loadSeriesDirectory(fullpath) ]
    
    return sorted(series, reverse=True)

def loadSeriesDirectory(dirname):
    '''Load a single single directory containing an info.json as described in the README'''

    infoFile   = os.path.join(dirname, "info.json")
    with open(infoFile) as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError as e:
            print("Failed to decode {} - {}".format(infoFile, e))
        return series.Series(data)
