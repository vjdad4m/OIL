import OIL.tools as tools
from OIL.color import Color, cGREEN
from OIL.label import Label

""" Image Tools """

# Image from @vajdaad4m on instagram
i = tools.OpenImage('images/image.jpg')

# Color conversion
i = tools.RGB2Gray(i)

# Resizing
print('Size before resize:', i.shape)
i = tools.Resize(i, 512, 512)
print('Size after resize:', i.shape)

# Display the image using opencv2
tools.ShowImage(i)

""" Colors """

red = Color(255, 0, 0)

print(red)
print(red.rgb)

print(cGREEN)   # You can use built in color codes

""" Labels """

lane = Label('lane', red)

print(lane)
print(lane.name)
print(lane.color)