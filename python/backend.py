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

    return filter(lambda e: simpleSelection.simpleFilter(e, tags), seriesList)

def search(inputString):
    if not seriesList:
        raise AssertionError("No database availiable (search)")
    return filter(lambda e: simpleSelection.simpleSearchFilter(e, inputString), seriesList)
