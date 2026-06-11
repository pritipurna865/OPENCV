import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    rotated = cv2.rotate(frame, cv2.ROTATE_180)

    h, w = rotated.shape[:2]

    resized = cv2.resize(rotated, (w//2, h//2))

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Gray Half Size", gray)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()