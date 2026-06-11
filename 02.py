import cv2
import time

cap = cv2.VideoCapture(0)

prev = time.time()

while True:
    ret, frame = cap.read()

    current = time.time()
    fps = 1/(current-prev)
    prev = current

    cv2.putText(frame, f"FPS: {int(fps)}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,(0,255,0),2)

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):
        cv2.imwrite("captured.jpg", frame)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()