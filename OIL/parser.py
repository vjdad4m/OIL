from OIL.errors import *
from OIL.color import Color, cWHITE
from OIL.label import Label

def LoadOIL(filename):
    data = []
    try:
        with open(filename) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line[0] != '#' and line[0] != '\n':
                    data.append(line[:-1])
    except:
        raise OILFileLoadError
    return data

def ParseOIL(data):
    raise NotImplementedError