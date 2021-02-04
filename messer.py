#!venv/bin/python

import cv2 as cv
from random import random
from scipy import ndimage
import numpy as np

img = cv.imread('images/panel.png')
print('image shape: ', img.shape)

# value of green and red in hsv
lower_green = np.array([45,40, 150])
upper_green = np.array([80,255,255])
lower_red = np.array([0,50, 50])
upper_red = np.array([3,255,255])

roi_x = 665
roi_y = 549
roi_ref_x = 515
roi_ref_y = 544

roi_width = 100
roi_height = 100

#### ROI ########
# watch the intensity of green in the roi to know when 
#  the subcooler fill valve is open
roi = img[roi_y: roi_y + roi_height, roi_x:roi_x + roi_width]

# draw roi border
marked_img = cv.rectangle(
	img, 
	(roi_x, roi_y), 
	(roi_x + roi_width, roi_y + roi_height), 
	(0,0,255), 
	3
)

# convert to hsv (hue-saturation-value) to pick out a color
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# blackout everything that isnt green
mask = cv.inRange(hsv, lower_green, upper_green)
green = cv.bitwise_and(roi, roi, mask=mask)
cv.imshow('roi', green)

# convert to grayscale (messy rgb pixel array becomes a scalar)
gray = cv.cvtColor(green, cv.COLOR_BGR2GRAY)
cv.imshow('roi gray', gray)


########### REFERENCE ROI ###########
# now do the same thing again for the supply valve to the mono
# allows to compare against what we know the valve will look like when opened
# also makes sure the camera hasnt moved so we have a valid image
roi_ref= img[roi_ref_y: roi_ref_y + roi_height, roi_ref_x:roi_ref_x + roi_width]

# draw reference roi border
marked_img = cv.rectangle(
	marked_img, 
	(roi_ref_x, roi_ref_y), 
	(roi_ref_x + roi_width, roi_ref_y + roi_height), 
	(255,0,0), 
	3
)

hsv_ref = cv.cvtColor(roi_ref, cv.COLOR_BGR2HSV)
mask_ref = cv.inRange(hsv_ref, lower_green, upper_green)
green_ref = cv.bitwise_and(roi_ref, roi_ref, mask=mask_ref)
cv.imshow('reference', green_ref)
gray_ref = cv.cvtColor(green_ref, cv.COLOR_BGR2GRAY)
cv.imshow('ref gray', gray_ref)

#####################################
# integrate the regions
grayrows = np.sum(gray, axis=0)
graysum = np.sum(grayrows, axis=0)
print(graysum)

grayrefrows= np.sum(gray_ref, axis=0)
grayrefsum = np.sum(grayrefrows, axis=0)
print(grayrefsum)

ratio = grayrefsum/graysum

if ratio < 40 and graysum > 60000:
	marked_img = cv.putText(marked_img, "OPEN", (800,250), cv.FONT_HERSHEY_SIMPLEX, 7, (0,0,255), 4, cv.LINE_AA)
else:
	marked_img = cv.putText(marked_img, "CLOSED", (800,250), cv.FONT_HERSHEY_SIMPLEX, 7, (0,0,255), 4, cv.LINE_AA)


cv.imshow('hi', marked_img)
k = cv.waitKey(0)



