import numpy as np
import cv2

image = cv2.imread("rama.jpg")  # BGR

#? RGB #
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # RGB
channels = cv2.split(image_rgb)

#! READ THIS #

cv2.imshow('Image', image)

# for c, label in zip(channels, list('RGB')):
#     print(label)
#     cv2.imshow(label, c)

lower_rgb = np.array([143, 2, 48])
upper_rgb = np.array([200, 120, 125])

mask = cv2.inRange(image_rgb, lower_rgb, upper_rgb)
masked_rgb = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Mased RGB', masked_rgb)
cv2.waitKey(0)

#?##########################
#?           HSV           #
#?##########################
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # HSV

#! READ THIS #


def hsv_from(rgb_value):
    rgb = np.uint8([[list(rgb_value)]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv[0][0][0]


lower_hsv = np.array([hsv_from(lower_rgb), 50, 50])
upper_hsv = np.array([hsv_from(upper_rgb), 255, 255])


mask = cv2.inRange(image_hsv, lower_hsv, upper_hsv)
masked_hsv = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Mased HSV', masked_hsv)
cv2.waitKey(0)
