import cv2
from pyzbar.pyzbar import decode

def decode_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
        return

    # Decode the codes
    decoded_objects = decode(image)
    if not decoded_objects:
        print("No codes detected in the image.")
        return

    # Print decoded information
    for obj in decoded_objects:
        print(f"Type: {obj.type}")
        print(f"Data: {obj.data.decode('utf-8')}")
        print("-" * 30)

# Provide the image path
image_file = "qrcode.png"  # Replace with your image file
decode_image(image_file)
