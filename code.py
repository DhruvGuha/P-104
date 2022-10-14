import cv2

ss = cv2.imread("solar-system.jpg")
#SUN
cv2.putText(ss,"Sun",(75,50),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255)) 
cv2.putText(ss,"Mercury",(128,190), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(ss,"Venus",(190,260), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(ss,"Earth",(285,270), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(ss,"Moon",(315,150), cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(ss,"Mars",(375,255), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(ss,"Jupiter",(480,100), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(ss,"Saturn",(700,120), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(ss,"Uranus",(950,140), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(ss,"Neptune",(1100,150), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("Solar System",ss)
cv2.waitKey(0)