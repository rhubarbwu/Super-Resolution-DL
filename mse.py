import matplotlib.pyplot as plt
import numpy as np

A = plt.imread("lfw/Lindsey_Graham/Lindsey_Graham_0002.jpg")
B = plt.imread("lfw/Lindsey_Graham/Lindsey_Graham_0001.jpg")

mse = ((A - B)**2).mean(axis=None)