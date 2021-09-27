import cv2

# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)
for i in range(47):
  print("No.={} parameter={}".format(i,cap.get(i)))
while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

  # 顯示圖片
  cv2.imshow('frame', frame)
  # 若按下 q 鍵則離開迴圈
  key = cv2.waitKey(1)
  if key == ord('s'):
    print(frame.shape)
  if key == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()