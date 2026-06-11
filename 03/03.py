import cv2

image = cv2.imread("image.jpeg") 

if image is None:
    print("Error: Could not find or load the image.")
else:
    
    height, width, channels = image.shape
    total_pixels = image.size 
    resolution_pixels = height * width
    
    print(f"--- Image Metadata ---")
    print(f"Dimensions: {width}x{height}")
    print(f"Total Pixel Values (Array Size): {total_pixels}")
    print(f"Total Resolution Pixels: {resolution_pixels}")
    
    
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, h=15, hColor=15, templateWindowSize=7, searchWindowSize=21)
    cv2.imwrite("denoised_result.jpg",denoised_image)
    print("Denoised image saved successfully as denoised_result.jpg'!")
    cv2.imshow("Original Noisy Image", image)
    cv2.imshow("Denoised Image Result", denoised_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()