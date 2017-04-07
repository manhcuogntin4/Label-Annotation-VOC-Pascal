import cv2
import numpy as numpy
import math
import imutils
img=cv2.imread("new2.png",1)
x1,y1=100,200
x2,y2=550,350
Alpha=math.radians(5)
t=math.atan(y1*1.0/x1)
#t=math.degrees(t)
#print "goc: ", t

y1_t=int(y1*math.cos(Alpha) + x1*math.sin(Alpha))
x1_t=int(x1*math.cos(Alpha) + y1*math.sin(Alpha)) 

x2_t=int(x2*math.cos(Alpha) + y2*math.sin(Alpha))
y2_t=int(y2*math.cos(Alpha) + x2*math.sin(Alpha))










print y1_t, x1_t, y2_t, x2_t


	

print (x2-x1)*math.cos(Alpha)
rect=cv2.rectangle(img, (x1, y1), (x2, y2), (255,255,0), 2)
w,h,d=rect.shape
cv2.imshow("rect", rect)
rows,cols, tt=img.shape
#M=cv2.getRotationMatrix2D((0, 0),10,1)
#dst=cv2.warpAffine(img,M, (cols,rows))
dst=imutils.rotate_bound(img,5)

w_n,h_n,d_n=dst.shape

print "size: ",w , w*math.sin(Alpha) + h*math.cos(Alpha), w_n, h_n

x1_n=int((x1*math.cos(Alpha)-y1*math.sin(Alpha)) + (w_n-y2*(1-math.tan(Alpha)))*math.sin(Alpha))
y1_n=int(x1*math.sin(Alpha)+y1*math.cos(Alpha))

x2_n=x1_n+int((x2-x1)*math.cos(Alpha)+(y2-y1)*math.sin(Alpha))
#x1_k=int(w_n*1.0/w)*x1_n


rect1=cv2.rectangle(dst, (x1_n, y1_t), (x2_n, y2_t), (0,255,0), 2)
cv2.imshow("rect1", rect1)



# r=h_n*1.0/h
# x1_t=x1_t-(w_n-w)

# x2_t=x2_t- (w_n-w)
# rect1=cv2.rectangle(dst, (x1_t, y1_t), (x2_t, y2_t), (0,255,0), 2)
# print "r=", r*(x2-x1)
# cv2.imshow("rect1", rect1)

# cv2.imwrite("result.png",dst)
# #cv2.imshow("img", dst)

# # Transformation
# x1_n=x1_t
# y1_n=y1_t
# x2_n=x2_t
# y2_n=y2_t
# print x1_n, y1_n, x2_n, y2_n, math.sin(Alpha), math.cos(Alpha)
# # Calcul bouding box
# x1_new=x1_n
# y1_new=y1_n-int((x2-x1)*math.sin(Alpha)) 
# x2_new=x1_n+int((x2-x1)*math.cos(Alpha)+(y2-y1)*math.sin(Alpha))
# y2_new=y1_n+int((y2-y1)*math.cos(Alpha))




# print x1_new,y1_new,x2_new, y2_new
# rect_new=cv2.rectangle(dst, (x1_new, y1_new), (x2_new,y2_new), (255,0,0), 2)
#cv2.imshow("rect_new", rect_new)
cv2.waitKey(0)