import matplotlib.pyplot as plt
import numpy as np

folder_name = "alexjc_neural-enhance/"

# images = [

# ]
# png vs jpg mse needs to be scaled

A =    plt.imread("alexjc_neural-enhance/salisbury-cathedral_ne2x_80.png")
B = plt.imread("small-test-set_processed/salisbury-cathedral.jpg")
A = A*256

mse = ((A - B)**2).mean(axis=None)#/(A.shape[0]*A.shape[1])

print (mse)