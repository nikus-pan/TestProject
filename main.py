import cv2
import pyttsx3

# 初始化 pyttsx3
engine = pyttsx3.init()

# 載入 Haar 級聯分類器
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

# 開啟攝影機
cap = cv2.VideoCapture(0)
last_num_faces = 0
    # 讀取一幀
    ret, frame = cap.read()

    # 轉換成灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測臉部
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 語音輸出臉部數量
    if len(faces) != last_num_faces:
        last_num_faces = len(faces)
        if len(faces) > 0:
            engine.say(f'偵測到 {len(faces)} 張臉')
            engine.runAndWait()

    for (x, y, w, h) in faces:
        # 繪製臉部矩形
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # 偵測眼睛
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # 繪製眼睛矩形
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # 顯示結果
    cv2.imshow('frame', frame)

    # 按下 'q' 鍵結束
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()
