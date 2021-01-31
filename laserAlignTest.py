#!venv/bin/python

"""
Experiment with finding a red object in a picture.
  First add a red object onto a background image in a random location.  
  Then process the image to independently find the location of the object.
"""



import cv2 as cv
from random import random
from scipy import ndimage
import numpy as np

################################################################
# Create a test image with a randomly placed frowning red target

img = cv.imread('images/yo.jpg')
img_rows, img_cols, img_num = img.shape

# for easy mode, black out the background before adding on the target image
#img[:,:,:] = 0

target = cv.imread('images/redThing.jpeg')
t_rows, t_cols, t_num = target.shape
print('target shape:, ', t_rows, t_cols)

roi_row = int(random() * img_rows)
roi_col = int(random() * img_cols)
roi_row = img_rows - t_rows if roi_row + t_rows > img_rows else roi_row
roi_col = img_cols - t_cols if roi_col + t_cols > img_cols else roi_col
print('roi pos: ', roi_row, roi_col)

img[roi_row:roi_row + t_rows, roi_col:roi_col + t_cols] = target

cv.imshow('target', img)
cv.imwrite('images/target.jpg', img)

################################################################
# Find the center of the target and draw a green circle on it

img = cv.imread('images/target.jpg')
print('image shape: ', img.shape)

# convert to hsv (hue-saturation-value) to pick out a color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# blackout everything that isnt red
lower_red = np.array([0,100,100])
upper_red = np.array([20,255,255])
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
