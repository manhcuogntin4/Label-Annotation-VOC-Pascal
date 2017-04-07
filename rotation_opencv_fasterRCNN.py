import cv2
import numpy as numpy
import math
img=cv2.imread("new2.png",1)
x1,y1=412,254
x2,y2=1000,310
Alpha=math.radians(5)
print (x2-x1)*math.cos(Alpha)
rect=cv2.rectangle(img, (x1, y1), (x2, y2), (255,255,0), 2)
cv2.imshow("rect", rect)
rows,cols, tt=img.shape
M=cv2.getRotationMatrix2D((0, 0),5,1)
dst=cv2.warpAffine(img,M, (cols,rows))
cv2.imwrite("result.png",dst)
cv2.imshow("img", dst)
# Transformation
x1_n=x1+ int(y1*math.sin(Alpha))
y1_n=y1-int(x1*math.sin(Alpha))
x2_n=x2+int(y2*math.sin(Alpha))
y2_n=y2-int(x2*math.sin(Alpha))
print x1_n, y1_n, x2_n, y2_n, math.sin(Alpha), math.cos(Alpha)
# Calcul bouding box
x1_new=x1_n
y1_new=y1_n-int((x2-x1)*math.sin(Alpha)) 
x2_new=x1_n+int((x2-x1)*math.cos(Alpha)+(y2-y1)*math.sin(Alpha))
y2_new=y1_n+int((y2-y1)*math.cos(Alpha))

print x1_new,y1_new,x2_new, y2_new
rect_new=cv2.rectangle(dst, (x1_new, y1_new), (x2_new,y2_new), (255,0,0), 2)
cv2.imshow("rect_new", rect_new)
cv2.waitKey(0)