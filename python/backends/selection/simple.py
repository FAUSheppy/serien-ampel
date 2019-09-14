def simpleFilter(series, tags):
    '''A very simple filter only looking for keywords in the genre string'''
    return any([tag in series.genre for tag in tags])

def simpleSearchFilter(series, string):
    '''A very simple search-selector'''

    inputString = string.lower()
    titleString = series.title.lower()
    return string in series.title or series.title in string
