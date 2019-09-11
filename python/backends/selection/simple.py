def simpleFilter(series, tags):
    '''A very simple filter only looking for keywords in the genre string'''
    return any([tag in series.genre.split() for tag in tags])
