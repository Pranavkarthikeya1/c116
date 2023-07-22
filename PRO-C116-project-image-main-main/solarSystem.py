import cv2
image=cv2.imread("solar-system.jpg")

cv2.putText(image,"sun",(20,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,255,0))
cv2.putText(image,"mercury",(100,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.putText(image,"venus",(200,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.putText(image,"earth",(300,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.putText(image,"mars",(400,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.putText(image,"jupiter",(600,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.putText(image,"saturn",(800,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.putText(image,"uranus",(1000,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.putText(image,"neptune",(1200,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(0,255,0))
cv2.imshow("image",image)
cv2.waitKey(0)