import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.85)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
canvas = None

xp, yp = 0, 0 

print("Instructions: \n1. Index finger up to DRAW.\n2. Index + Middle finger up to HOVER/MOVE.\n3. Press 's' to SAVE.\n4. Press 'q' to QUIT.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
        
    frame = cv2.flip(frame, 1) 
    h, w, c = frame.shape
    
    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)


    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            # Extract landmarks for Index (8), Middle (12) tips and roots (6, 10)
            lm = hand_lms.landmark
            x8, y8 = int(lm[8].x * w), int(lm[8].y * h)
            x12, y12 = int(lm[12].x * w), int(lm[12].y * h)
            
            index_up = lm[8].y < lm[6].y
            middle_up = lm[12].y < lm[10].y
            
            if index_up and not middle_up:
                cv2.circle(frame, (x8, y8), 10, (0, 255, 0), cv2.FILLED)
                if xp == 0 and yp == 0:
                    xp, yp = x8, y8
                
                cv2.line(canvas, (xp, yp), (x8, y8), (255, 255, 255), 5)
                xp, yp = x8, y8
            elif index_up and middle_up:
               
                xp, yp = 0, 0
                cv2.circle(frame, (x8, y8), 10, (0, 0, 255), cv2.FILLED)
            else:
                xp, yp = 0, 0
                 
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, img_inv)
    frame = cv2.bitwise_or(frame, canvas)
    
    cv2.imshow("Virtual Drawing Board", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('s'):
        cv2.imwrite("my_drawing.png", canvas)
        print("Drawing saved as 'my_drawing.png'!")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()