import cv2
import numpy as np

img = cv2.imread("mountain_lake.jpeg")

if img is None:
    print("Error: Could not locate the mountain lake image.")
else:
  
    b, g, r = cv2.split(img)
    blank = np.zeros_like(b)
    
   
    blue_img = cv2.merge([b, blank, blank])
    green_img = cv2.merge([blank, g, blank])
    red_img = cv2.merge([blank, blank, r])
    
   
    merged_no_green = cv2.merge([b, blank, r])
    
    
    cv2.imshow("Original Blue Channel", blue_img)
    cv2.imshow("Original Green Channel", green_img)
    cv2.imshow("Original Red Channel", red_img)
    cv2.imshow("Merged Output (No Green Channel)", merged_no_green)
    

    cv2.imwrite("channel_blue.png", blue_img)
    cv2.imwrite("channel_green.png", green_img)
    cv2.imwrite("channel_red.png", red_img)
    cv2.imwrite("merged_no_green.png", merged_no_green)
    
    print("All channels and merged outputs saved successfully.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()