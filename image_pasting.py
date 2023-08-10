import cv2
import numpy as np
from PIL import Image, ImageFilter


img = cv2.imread("C:\\Users\\KESHAV TRIKHA\\OneDrive\\Desktop\\TWD\\jw.jpeg")
img2 = cv2.imread("C:\\Users\\KESHAV TRIKHA\\OneDrive\\Desktop\\TWD\\tm.jpeg")
rows, cols, _ = img2.shape
print("Rows", rows)
print("Columns", cols)
x, y = 6, 150
cut_img = img[54:410, 540:845]

for i in range(cut_img.shape[0]):
    for j in range(cut_img.shape[1]):
        if x + i < img2.shape[0] and y + j < img2.shape[1]:
            img2[x + i, y + j] = cut_img[i, j]
cv2.imshow("Image",img2)
cv2.waitKey(0)
