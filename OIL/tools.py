import cv2
import numpy as np
from PIL import Image

def OpenImage(filename):
    img = Image.open(filename)
    img = np.array(img)
    img = BGR2RGB(img)
    return img

def ShowImage(image, win_name = 'CV2Image'):
    # TODO: Better implementation of this function
    cv2.imshow(win_name, image)
    while True:
        if (cv2.getWindowProperty(win_name, cv2.WND_PROP_VISIBLE) < 1):
            break
        if cv2.waitKey(100) == 27:  # Escapes
            break        
    cv2.destroyAllWindows()

def RGB2Gray(image):
    img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return img

def BGR2RGB(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return img

def Resize(image, new_w, new_h):
    img = cv2.resize(image, (new_w, new_h))
    return img