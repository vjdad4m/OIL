import OIL.tools as tools
from OIL.color import Color, cGREEN
from OIL.label import Label
from OIL.parser import LoadOIL, ParseOIL
from OIL.errors import *

""" Image Tools """

# Image from @vajdaad4m on instagram
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

try:
    LoadOIL('asd')
except OILFileLoadError:
    print('File Load error') # This should happen, as 'asd' does not exist

data = LoadOIL('./images/labels/image.oil')
print('before parsing: ')
print(data)

print()
print()

parsed = ParseOIL(data)
print('Parsed: ')
print(parsed)

# TODO: Implement method to convert parsed data to image data
