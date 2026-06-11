import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
led_on = False
pinch_cooldown = False 

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
        
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            
            thumb = hand_lms.landmark[4]
            index = hand_lms.landmark[8]
            
            
            tx, ty = int(thumb.x * w), int(thumb.y * h)
            ix, iy = int(index.x * w), int(index.y * h)
            
           
            distance = math.hypot(tx - ix, ty - iy)
         
            if distance < 30:
                if not pinch_cooldown:
                    led_on = not led_on  
                    pinch_cooldown = True
            else:
                pinch_cooldown = False 
                
           
            cv2.circle(frame, (tx, ty), 6, (255, 0, 0), cv2.FILLED)
            cv2.circle(frame, (ix, iy), 6, (255, 0, 0), cv2.FILLED)

    
    color = (0, 255, 0) if led_on else (0, 0, 255)
    label = "LED State: ON" if led_on else "LED State: OFF"
    
    cv2.circle(frame, (60, 60), 25, color, cv2.FILLED)
    cv2.putText(frame, label, (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    cv2.imshow("Hand Pinch LED Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()