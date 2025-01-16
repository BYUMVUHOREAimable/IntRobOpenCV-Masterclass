import cv2  # Import OpenCV library

# Read the image 'lena_small.jpg'
image = cv2.imread('lena_small.jpg')

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (188, 188), bottom-right (376, 376)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 2 pixels

cv2.rectangle(image, (188, 188), (376, 376), (0, 255, 0), 2)

# Draw a red circle on the image
# Center coordinates: (282, 282), Radius: 94
# Color: Red (BGR format: (0, 255, 0)), Thickness: 2 pixels
cv2.circle(image, (282, 282), 94, (0, 0, 255), 2)

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
