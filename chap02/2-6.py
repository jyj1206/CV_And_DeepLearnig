# 영상에 도형을 그리고 글자 쓰기
import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv.rectagnle(img, (830,30), (1000, 200),(0,0,255),2) # 직사각형 그리기
cv.putText(img, 'laugh', (830,24), cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2) # 글자 쓰기

cv.imshow("Draw", img)

cv.waitKey()
cv.destroyAllWindows()