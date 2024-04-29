import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt


img  = cv2.imread(r"C:\Users\Lenovo\Documents\data science\image-classification\images\virat_kohli\4e43503188864ae8c588de0933f83ac104103451.png")

print(img.shape)
plt.imshow(img)