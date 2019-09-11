import python.backends.db.filesystem    as fs
import python.backends.selection.simple as simpleSelection


seriesList = None

BACKEND_FS = "FS"
BACKEND_FS_DEFAULT = "db"

def loadDB(backend=BACKEND_FS):
    if backend == BACKEND_FS:
        seriesList = fs.loadDirectory(BACKEND_FS_DEFAULT)

def suggest(tags, user=None):
    if user:
        raise NotImplementedError()
    if not seriesList:
        raise AssertionError("No database availiable")
    
    return filter(lambda e: simpleSelection.simpleFilter(e, tags), seriesList)
