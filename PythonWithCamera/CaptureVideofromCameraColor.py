# encoding: utf-8
import cv2

print ("OpenCV Version : " + cv2.__version__)

video_capture = cv2.VideoCapture(1)

if video_capture.isOpened():
    print ("Camera was opened")
else:
    video_capture.open(0)
    print ("Restart camera")

# 顯示所有視訊相關參數
for i in range(0,18):
    print (video_capture.get(i))

# 重新設定解析度
#ret = video_capture.set(3,320)
#ret = video_capture.set(4,240) 

while (True):
    # 擷取即時串流影像
    ret, frame = video_capture.read()

    # 顯示擷取影像
    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放記憶體
video_capture.release()
cv2.destroyAllWindows()
