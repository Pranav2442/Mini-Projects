
import cv2 as cv
import numpy as np




imgcolor=cv.imread("python\d84584e64ab8d30cbcbcd19269bd98c7.jpg")
imgresized=cv.resize(imgcolor,(512,512))

imgclear=cv.medianBlur(imgresized,3)
imgclear=cv.medianBlur(imgresized,3)
imgclear=cv.medianBlur(imgresized,3)

edgepre=cv.edgePreservingFilter(imgclear,sigma_s=5)

imgfilter=cv.bilateralFilter(imgclear,3,20,10)

for i in range(2):
    imgfilter=cv.bilateralFilter(imgclear,5,40,10)
for i in range(2):
    imgfilter=cv.bilateralFilter(imgclear,3,40,10)
for i in range(2):
    imgfilter=cv.bilateralFilter(imgclear,3,40,5)



gausianblurfor=cv.GaussianBlur(imgfilter,(7,7),2)
imagesharp=cv.addWeighted(imgfilter,1.5,gausianblurfor,-0.5,0)
imagesharp=cv.addWeighted(imgfilter,1.4,gausianblurfor,-0.2,10)

cv.imshow("watercolor",imagesharp)
# cv.imshow("Original",imgcolor)
cv.imshow("original",imgresized)
cv.waitKey(0)



























import cv2 as cv
import numpy as np

capturedvi=cv.VideoCapture(0)
openedvif=capturedvi.isOpened()
if(openedvif):
    while(capturedvi.isOpened()):
        retre,eachframe=capturedvi.read()
        if(retre==True):
            eachframemedblur=cv.medianBlur(eachframe,5)
            eachframemedblur=cv.medianBlur(eachframe,5)
            eachframemedblur=cv.medianBlur(eachframe,5)

            edgepres=cv.edgePreservingFilter(eachframemedblur,sigma_s=5)
            eachframed=cv.bilateralFilter(edgepres,3,20,10)

            for i in range(2):
                imgfilter=cv.bilateralFilter(eachframed,5,40,10)
            for i in range(2):
                imgfilter=cv.bilateralFilter(eachframed,3,40,10)
            for i in range(2):
                imgfilter=cv.bilateralFilter(eachframed,3,40,5)

            gausianblurforeachframed=cv.GaussianBlur(eachframed,(7,7),2)
            imagesharp=cv.addWeighted(imgfilter,1.5,gausianblurforeachframed,-0.5,0)
            imagesharp=cv.addWeighted(imgfilter,1.4,gausianblurforeachframed,-0.2,10)
            cv.imshow("img",imagesharp)
            if(cv.waitKey(2)==27):
                break
capturedvi.release()            
cv.destroyAllWindows()