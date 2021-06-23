import OIL.tools as tools
from OIL.color import Color, cGREEN
from OIL.label import Label, PaletteToLabel
from OIL.parser import *
from OIL.errors import *


import OIL
""" Image Tools """

# Image from @vajdad4m on instagram
# i = tools.OpenImage('images/image.jpg')

# Color conversion
# i = tools.RGB2Gray(i)

# Resizing
# print('Size before resize:', i.shape)
# i = tools.Resize(i, 512, 512)
# print('Size after resize:', i.shape)

# Display the image using opencv2
# tools.ShowImage(i)
# TODO: fix ShowImage() -> Program should continue running, not wait

""" Colors """

# red = Color(255, 0, 0)

# print(red)
# print(red.rgb)

# print(cGREEN)   # You can use built in color codes

""" Labels """

# l1 = Label('lane', red)

# print(l1)
# print(l1.name)
# print(l1.color)

""" Parser """

file_name = './images/labels/image.oil'

"""
try:
    LoadOIL('asd')
except OILFileLoadError:
    print('File Load error') # This should happen, as 'asd' does not exist
"""

# Use theese to load OIL step-by-step:

# data = LoadOIL('./images/labels/image.oil')
# print('before parsing: ')
# print(data)

# parsed = ParseOIL(data)
# print('Parsed: ')
# print(parsed)

# image = ParseToImage(parsed)
# print(image)
# tools.ShowImage(image)

# Use only to display, as other data is not loaded by this function:

# img = OILToImage(file_name)
# tools.ShowImage(img)

# Use this to extract specific label:

parse_data = ParseOIL(LoadOIL(file_name))
palette = ParseToPalette(parse_data)
print(palette)
labels = PaletteToLabel(palette)
l = labels[2] # Extract only green
data = ExtractSpecificLabel(parse_data, l)
# print(data)
tools.ShowImage(data)