import cv2
import os
import numpy as np

os.makedirs("./calib/left_gray",exist_ok=True)
# for i in range(1,19):
#   img = cv2.imread("./calib/left/%d.png"%i,0)
  # cv2.imwrite("./calib/left_gray/%d_gray.png"%i, img)
img = cv2.imread("./pig.png",0)
img_color = cv2.applyColorMap(np.uint8(img*0.7),cv2.COLORMAP_HSV)
cv2.imwrite("./pig_hsv1.png", img_color)