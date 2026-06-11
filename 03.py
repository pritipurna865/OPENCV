import cv2

img = cv2.imread("image.jpg")

denoised = cv2.GaussianBlur(img, (5,5), 0)

height, width, channels = img.shape
pixels = height * width

print("Total Pixels =", pixels)

cv2.imshow("Original", img)
cv2.imshow("Denoised", denoised)

cv2.waitKey(0)
cv2.destroyAllWindows()