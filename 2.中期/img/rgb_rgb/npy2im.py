import cv2
import os
import numpy as np
import glob

npy_list = glob.glob("./rgb_rgb/*.npy")
os.makedirs("./rgb_rgb/png", exist_ok=True)
i = 0
for file in npy_list:
  i += 1
  npy = np.load(file)
  print(np.max(npy),np.min(npy))
  npy = npy/np.max(npy)
  im = cv2.applyColorMap(np.uint8(npy*255), cv2.COLORMAP_JET)
  cv2.imwrite("./rgb_rgb/png/{}.png".format(i), im)