def greedyTagScored(seriesList, tags):
    '''A very simple rank based on tags and score'''
    retDict = dict()
    for series in seriesList:
        if any([tag in series.genre for tag in tags]):
            if series in retDict:
                retDict[series] *= 2
            else:
                retDict.update({series:series.score})

    # normalize for many-tag series #
    if not len(tags) == 1:
        for series in retDict.keys():
            seriesTagsNotInQuery = len(list(filter(lambda x: x not in tags, series.genre)))
            queryTagsNotInSeries = len(list(filter(lambda x: x not in series.genre, tags)))
            retDict[series] /= max(1, max(queryTagsNotInSeries, seriesTagsNotInQuery))

    tupelList       = list(zip(retDict.keys(), retDict.values()))
    sortedTupelList = sorted(tupelList, key=lambda x: x[1], reverse=True)
    return [x[0] for x in sortedTupelList]

def simpleSearchFilter(series, string):
    '''A very simple search-selector'''

    inputString = string.lower()
    titleString = series.title.lower()
    return string in series.title or series.title in string
