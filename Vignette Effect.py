import cv2 as cv
import numpy as np

def focus(var):
	global val
	val = var




def radius(val):
	global rad
	rad = val
	

val = 1
rad = 120



img = cv.imread('python\me.jpeg')
r, c = img.shape[:2]


mask = np.zeros((int(r*(val*0.1+1)),int(c*(val*0.1+1))))
cv.namedWindow('Customize_Window')
cv.createTrackbar('Radius', 'Customize_Window', 100, 600, radius)
cv.createTrackbar('Focus', 'Customize_Window', 1, 20, focus)

while(True):
	
	kernel_v = cv.getGaussianKernel(int(c*(0.1*val+1)),rad)
	kernel_h = cv.getGaussianKernel(int(r*(0.1*val+1)),rad)
	kernel = kernel_h* kernel_v.T
	
	
	kernel = kernel/np.linalg.norm(kernel)	
	
	
	maskimage = 255 * kernel
	output = np.copy(img)
	
	maskcropped = maskimage[int(0.1*val*r):,int(0.1*val*c):]
	for i in range(3):
		output[:,:,i] = output[:,:,i] * maskcropped
		resizedimage=cv.resize(output,(720,720))
		resizedoriginalimage=cv.resize(img,(512,512))
	cv.imshow('Vignette', resizedimage)
	cv.imshow("Original",resizedoriginalimage)
	if(cv.waitKey(2)==27):
		break
	

