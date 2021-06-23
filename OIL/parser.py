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