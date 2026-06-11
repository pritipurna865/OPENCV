import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
        
   
    frame = cv2.flip(frame, 1)
    
    h, w, c = frame.shape
  
    qw, qh = int(w / 2), int(h / 2)
    
    
    top_left = cv2.resize(frame, (qw, qh))
    
    
    top_right = cv2.flip(top_left, 0)
    
    
    bottom_left_hsv = cv2.cvtColor(top_left, cv2.COLOR_BGR2HSV)
    
    
    b, g, r = cv2.split(top_left)
    blank = np.zeros_like(b)
    bottom_right_red = cv2.merge([blank, blank, r])
    
   
    top_row = np.hstack((top_left, top_right))
    bottom_row = np.hstack((bottom_left_hsv, bottom_right_red))
    combined_grid = np.vstack((top_row, bottom_row))
    
    cv2.imshow("4-Quadrant Channel Configuration Feed", combined_grid)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()