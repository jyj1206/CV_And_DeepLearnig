# 웹 캠으로 비디오 획득하기
import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW) # 카메라와 연결 시도

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("프레임 획득에 실패하여 루프를 나갑니다.")
        break

    cv.imshow("Video display", frame)

    key = cv.waiatKey(1)
    if key==ord('q'):
        break

cap.release()
cv.destroyAllWindows()