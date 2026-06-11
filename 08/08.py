import cv2

#Operation1:Loading the image
frame = cv2.imread("robot_vision.jpg")

#operatin2: converting clor space
gray_frame = cv2.cvtColor(frame,cv2.COLOR_BAYER_BGR2GRAY)

#operation3: Drawing a bounding box
gray_frame = cv2.rectangle(gray_frame,(10,10),(100,100),(0,255,0),3)

#Operation4: Displaying the result
cv2.imshow("Robot vision",gray_frame)
cv2.waitKey()

'''
Statement A is INCORRECT: By default, OpenCV's cv2.imread() loads images in BGR (Blue, Green, Red) format order, not standard RGB. 

Statement B is CORRECT: Since the canvas was converted to a single-channel grayscale structure in Operation 2, 
                        any geometric drawing attempt passing a color tuple like (0, 255, 0) will fail to display color. 
                        It maps down to a singular grayscale intensity value representation instead.  
 
Statement C is CORRECT: Passing 1 into cv2.waitKey() pauses for exactly 1 millisecond before moving to execution completion.
                        For static photos, a value of 0 is required to yield an infinite user input wait block.  
 
Statement D is INCORRECT: In cv2.rectangle(), the dual coordinate tuples denote the Top-Left Corner vertex and the Bottom-Right Corner vertex points,
                          not centromeres or scale properties.  
'''