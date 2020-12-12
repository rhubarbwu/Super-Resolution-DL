import matplotlib.pyplot as plt
import numpy as np
import sys

# A = plt.imread(sys.argv[1])
# B = plt.imread(sys.argv[2])

A = plt.imread("small-test-set_processed/salisbury-cathedral.jpg")
B =                  plt.imread("opencv_/salisbury-cathedral.jpg")

# if ".png" in sys.argv[1]:
#     A *= 256
# if ".png" in sys.argv[2]:
#     B *= 256

mse = ((A - B)**2).mean(axis=None)

print(mse)
