import python.backends.database.filesystem as fs
import python.backends.selection.simple    as simpleSelection


seriesList = None

BACKEND_FS = "FS"
BACKEND_FS_DEFAULT = "db"

def loadDB(backend=BACKEND_FS):
    global seriesList

    if backend == BACKEND_FS:
        seriesList = fs.loadDbDirectory(BACKEND_FS_DEFAULT)

def suggest(tags, user=None):
    if user:
        raise NotImplementedError()
    if not seriesList:
        raise AssertionError("No database availiable (suggest)")

    return simpleSelection.greedyTagScored(seriesList, tags)

def search(inputString):
    if not seriesList:
        raise AssertionError("No database availiable (search)")
    return filter(lambda e: simpleSelection.simpleSearchFilter(e, inputString), seriesList)

def getFilters(limit=100):
    if not seriesList:
        raise AssertionError("No database availiable (filters)")

    filters = dict()
    for e in seriesList:
        for tag in e.genre:
            if tag in filters:
                filters[tag] += 1
            else:
                filters.update( { tag : 1 })
    
    filtersSortedByFrequency = sorted(list(zip(filters.keys(), filters.values())), key=lambda x: x[1])
    return sorted([ x[0] for x in filtersSortedByFrequency][:limit])
        
def getReason():
    raise NotImplementedError()
