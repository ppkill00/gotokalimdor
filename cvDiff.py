import cv2
import numpy as np
from matplotlib import pyplot as plt


def cvdiffv1(screen, template, method):
    point = ()
    img = cv2.imread(screen,0)
    img2 = img.copy()
    template = cv2.imread(template,0)
    w, h = template.shape[::-1]
    # print("%d %d" %(w,h))
    # All the 6 methods for comparison in a list
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']    
    img = img2.copy()
    method = eval(method)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print("top_left : " + str(top_left))
    print("bottom_right : " + str(bottom_right))
    point = ((bottom_right[0] - top_left[0])/2+top_left[0], bottom_right[1]-(bottom_right[1] - top_left[1])/2)
    print("center point: " + str(point))
    return point
