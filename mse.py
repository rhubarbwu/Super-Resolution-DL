import matplotlib.pyplot as plt
import numpy as np
import sys

A = plt.imread(sys.argv[1])
B = plt.imread(sys.argv[2])

if ".png" in sys.argv[1]:
    A *= 256
if ".png" in sys.argv[2]:
    B *= 256

mse = ((A - B)**2).mean(axis=None)

print(mse)
