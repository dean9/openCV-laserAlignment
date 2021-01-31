#!venv/bin/python

"""
As a follow up on laserAlignmentTest, try the same red object finding process 
on a real image from the beamline.
"""

import cv2 as cv
from random import random
from scipy import ndimage
import numpy as np

# try to analyze the picture of the vortex

img = cv.imread('images/vortexFace.png')
print('image shape: ', img.shape)

# convert to hsv (hue-saturation-value) to pick out a color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# blackout everything that isnt red
lower_red = np.array([0,50, 50])
upper_red = np.array([3,255,255])
mask = cv.inRange(hsv, lower_red, upper_red)

red = cv.bitwise_and(img, img, mask=mask)
cv.imshow('red', red)

gray = cv.cvtColor(red, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# find center of mass
com_row, com_col = ndimage.measurements.center_of_mass(gray)
com_row = int(com_row)
com_col = int(com_col)
print("com pos: ", com_row, com_col)

marked_img = cv.circle(img, (com_col, com_row), 20, (0,255,0), -1)

cv.imshow('hi', marked_img)
k = cv.waitKey(0)
