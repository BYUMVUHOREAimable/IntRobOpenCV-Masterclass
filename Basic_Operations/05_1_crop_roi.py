import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena_small.jpg')

# Crop a region from the image
# Format: image[y0:y1, x0:x1]
#e.g. Crop height (i.e. y) from y0=188 to y1=376, width (i.e x) from x0=188 to x1=376
cropped_image = image[188:376, 188:376] 

# Display the cropped image in a window
cv2.imshow('Image', cropped_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the cropped region as a new image
cv2.imwrite('lena_cropped.jpg', cropped_image)

# Close all OpenCV windows
cv2.destroyAllWindows()
