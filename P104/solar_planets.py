import cv2
img=cv2.imread("C:/Users/Yuvika/Desktop/Python/Projects/P104/PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg")       
textshow="Sun"
cv2.putText(img,textshow,(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
textshow="mercury"
cv2.putText(img,textshow,(100,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
textshow="Venus"
cv2.putText(img,textshow,(200,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.imshow("solar-system",img)
cv2.waitKey(0)