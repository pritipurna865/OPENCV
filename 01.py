import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw = mp.solutions.drawing_utils

prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            x = int(hand.landmark[8].x * 640)
            y = int(hand.landmark[8].y * 480)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            cv2.line(canvas, (prev_x, prev_y), (x, y), (0,255,0), 5)
            prev_x, prev_y = x, y

    output = cv2.add(frame, canvas)

    cv2.imshow("Drawing Board", output)

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite("drawing.png", canvas)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()