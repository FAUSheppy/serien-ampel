def greedyTagScored(seriesList, tags):
    '''A very simple rank based on tags and score'''
    retDict = dict()
    for series in seriesList:
        if any([tag in series.genre for tag in tags]):
            if series in retDict:
                retDict[series] += series.score
            else:
                retDict.update({series:series.score})

    # normalize for many-tag series #
    # norm = max(3, len(series.genre))
    # for series in retDict.keys():
    #     retDict[series] /= norm

    tupelList       = list(zip(retDict.keys(), retDict.values()))
    sortedTupelList = sorted(tupelList, key=lambda x: x[1], reverse=True)
    return [x[0] for x in sortedTupelList]

def simpleSearchFilter(series, string):
    '''A very simple search-selector'''

    inputString = string.lower()
    titleString = series.title.lower()
    return string in series.title or series.title in string
