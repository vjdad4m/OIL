<center>
<big>

## OIL
### Open Image Labeling
---

</center>
<br/>

OIL is an open-source image labeling library. The project is inspired by [Comma AI's comma10k dataset](https://github.com/commaai/comma10k).

### The final product

You can load your own image, define your custom labels e.g: foreground, background. Then you open the LabelingGUI and mark each region of the image. Then you can save the labeled image to a custom file for labels. Theese label files shouldn't be much larger, than the original image. The extra information is the region coding, as the user can extract only a specific region e.g. self-driving cars need lane data, the sky label is useless in that case.

<br/>
<b>

### Currently working on:

</b>

* Easy-to-use label file loader
* Labeling GUI
* Better Implementations of already existing functions

Check ./test.py to see most recent features in action.

<br/>

---

## Contributions:
Contributions are greatly appreciated :) . If you want to get started, check the <b>TODO</b>'s in the code.

<br/>

## Installation

You need to have [python 3.8 or grater](https://www.python.org/downloads/) installed.

Download source and run this in your terminal:
```
pip install .
```
<br/>

<i>
p.s. Logo designs are appreciated, so feel free to make one.
</i>