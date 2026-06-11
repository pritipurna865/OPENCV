import cv2
import time

cap = cv2.VideoCapture(0)
p_time = 0
img_counter = 0

print("Instructions:\n1. Press SPACEBAR to capture/save image.\n2. Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
   
    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    
    
    cv2.putText(frame, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Webcam Live Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord(' '):
        img_name = f"snapshot_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"Saved: {img_name}")
        img_counter += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()