import cv2
import numpy as np
from matplotlib import pyplot as plt

import sys

img0 = cv2.cvtColor(cv2.imread(sys.argv[1],), cv2.COLOR_BGR2GRAY)
img0 = cv2.GaussianBlur(img0, (3, 3), 0)
img0_sobel = (cv2.Sobel(img0, cv2.CV_64F, 1, 0, ksize=5),
              cv2.Sobel(img0, cv2.CV_64F, 0, 1, ksize=5))


img1 = cv2.cvtColor(cv2.imread(sys.argv[2],), cv2.COLOR_BGR2GRAY)
if img1.shape != img0.shape:
    img1 = cv2.resize(img1, img0.shape)
img1 = cv2.GaussianBlur(img1, (3, 3), 0)
img1_sobel = (cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=5),
              cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=5))


plt.subplot(3, 3, 1), plt.imshow(img0, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 2), plt.imshow(img0_sobel[0], cmap='gray')
plt.title('Original SobelX'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 3), plt.imshow(img0_sobel[1], cmap='gray')
plt.title('Original SobelY'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 4), plt.imshow(img1, cmap='gray')
plt.title('Upscaled'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 5), plt.imshow(img1_sobel[0], cmap='gray')
plt.title('Upscaled SobelX'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 6), plt.imshow(img1_sobel[1], cmap='gray')
plt.title('Upscaled SobelY'), plt.xticks([]), plt.yticks([])

sq_err_sobel_x = (img0_sobel[0]-img1_sobel[0])**2
sq_err_sobel_y = (img0_sobel[1]-img1_sobel[1])**2

print("MSE Sobel X", np.average(sq_err_sobel_x))
print("MSE Sobel Y", np.average(sq_err_sobel_y))


plt.show()

