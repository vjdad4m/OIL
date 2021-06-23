from OIL.errors import *
from OIL.color import Color, cWHITE
from OIL.label import Label
from OIL.tools import BGR2RGB
import numpy as np

def LoadOIL(filename):
    data = []
    try:
        with open(filename) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line[0] != '#' and line[0] != '\n':
                    data.append(line.strip('\n'))
    except:
        raise OILFileLoadError
    return data

def ParseOIL(data):
    # File structure: * check images/labels/image.oil *
    # File starts with D, then next lines start with L's
    # After the labels, there is an I, then the image data.
    # Any other order should raise an OILFileParseError,
    # If there is unrecognized data, then raise OILFormatError.
    
    looking_for = 'D'
    parsed_data = {'size':0, 'labels':[], 'image':[]}
    for d in data:
        if d[0] == 'D' and looking_for == 'D':
            try:
                parsed_data['size'] = tuple(map(int,d[2:].split()))
            except:
                raise OILFormatError(data=d)
            looking_for = 'L'
        elif d[0] == 'L' and looking_for == 'L':
            try:
                l = d[2:].split()
                l[0] = l[0].strip("'")
                l[1], l[2], l[3] = int(l[1]), int(l[2]), int(l[3])
                lab = Label(l[0], Color(l[1], l[2], l[3]))
                parsed_data['labels'].append(lab)
            except:
                raise OILFormatError(data=d)
        elif d[0] == 'I' and looking_for == 'L':
            looking_for = 'I'
        elif looking_for == 'I':
            parsed_data['image'].append(d.split())
        else:
            raise OILParseError

    width, height = parsed_data['size']
    if len(parsed_data['image']) != height:
        raise OILFormatError(f"Invalid size data: {len(parsed_data['image'])} != {height}")
    for i in parsed_data['image']:
        if len(i) != width:
            raise OILFormatError(f"Invalid size data: {len(i)} != {width}")
    
    return parsed_data

def ParseToPalette(data):
    # Input data is returned from ParseOIL()
    palette = {'0': cWHITE.rgb}
    for c in data['labels']:
        palette[c.name] = c.color.rgb
    return palette

def ParseToImage(data):
    try:
        palette = ParseToPalette(data)
        width, height = data['size']
        img = np.zeros((width, height, 3))
        for y in range(height):
            for x in range(width):
                img[y][x] = palette[data['image'][y][x]]
        img = np.float32(img)
        img = BGR2RGB(img)
        return img
    except:
        raise ImageParseError
    return None

def OILToImage(filename):
    data = LoadOIL(filename)
    data = ParseOIL(data)
    data = ParseToImage(data)
    return data

def ExtractSpecificLabel(parse, label):
    # Input is a parse and a specific label
    try:
        palette = ParseToPalette(parse)
        width, height = parse['size']
        img = np.zeros((width, height, 3))
        for y in range(height):
            for x in range(width):
                img[y][x] = cWHITE.rgb
                l_name = parse['image'][y][x]
                if l_name == label.name:
                    l_color = palette[l_name]
                    if l_color == label.color:
                        img[y][x] = l_color                
        img = np.float32(img)
        img = BGR2RGB(img)
        return img
    except:
        raise ImageParseError
    return None