# 영상 파일을 읽고 윈도우에 디스플레이하기
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv.imshow("Image Display", img)

cv.waitKey()
cv.destroyAllWindows()