import numpy as np
import pandas as pd
from PIL import Image
from typing import Sequence


def _calc_likeness(pixel1: Sequence, 
                   pixel2: Sequence,
                   color_only=False):
    
    color_lik = list()
    for a, b in zip(pixel1, pixel2):
        c = (b/a) if (a >= b) else ((b-a)/a)
        color_lik.append(c)
    
    if color_only:
        return color_lik
    return np.mean(color_lik)
    
    

def template_match(img1: Image.Image, 
                   img2: Image.Image):
    
    arr1 = np.array(img1.getdata())
    arr2 = np.array(img2.getdata())
    np.reshape(arr1, (*img1.size, 3))
    np.reshape(arr2, (*img2.size, 3))
    
    # TODO: Discover some way of aligning everything
    return arr2



if __name__ == '__main__':
    img1 = Image.open('testing/myroom.jpg')
    img2 = Image.open('testing/myposter.jpg')
    print(template_match(img1, img2))
 