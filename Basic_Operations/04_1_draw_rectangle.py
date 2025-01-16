import cv2  # Import OpenCV library

# Read the image 'lena_small.jpg'
image = cv2.imread('lena_small.jpg')

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (188, 188), bottom-right (376, 376)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 2 pixels

cv2.rectangle(image, (188, 188), (376, 376), (0, 255, 0), 2)

# Display the image in a new window named 'Image'
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_rectangle.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()