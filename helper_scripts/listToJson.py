#!/usr/bin/python3
import sys
import os
import json

def lineToDict(lineArrFiltered):
    ret = dict()

    complete = False
    if "(complete)" in lineArrFiltered:
        complete = True
        lineArrFiltered.remove("(complete)")

    print(lineArrFiltered)
    title  = lineArrFiltered[0]
    season = lineArrFiltered[1]
    score  = lineArrFiltered[2]
    genre  = lineArrFiltered[3]

    ret.update( { "title"     : title        } )
    ret.update( { "season"    : season       } )
    ret.update( { "score"     : float(score) } )
    ret.update( { "genre"     : genre        } )
    ret.update( { "complete"  : complete     } )

    return ret


if __name__ == "__main__":

    filename    = "SeriesRecommendations.txt"
    
    lines       = open(filename, "r").read().replace("[", "").replace("]","").split("\n")
    linesSplit  = [ list(filter(lambda x: x, x.split("  "))) for x in lines ]
    linesFilter = filter(lambda x: len(x) >= 4, linesSplit)
    linesFilter = [ list(map(lambda a: a.strip(), x)) for x in linesFilter ]
    
    for arr in linesFilter:
        series    = lineToDict(arr)
        targetDir = "db/" + series["title"]
        if not os.path.isdir(targetDir):
            os.mkdir(targetDir)
            with open(targetDir + "/" + "info.json", "w") as f:
                f.write(json.dumps(series, indent=4, sort_keys=True))
