import cv2
import numpy as np
import subprocess
import os

# Paths to required files
javase_jar = "javase-3.5.0.jar"
core_jar = "core-3.5.0.jar"
jcommander_jar = "jcommander-1.82.jar"

# Input barcode image (can be passed as an argument or hardcoded)
barcode_image = "pdf417_code.png"  # Replace with your image path or use sys.argv to pass it

# Validate required files
for file in [javase_jar, core_jar, jcommander_jar, barcode_image]:
    if not os.path.exists(file):
        print(f"Error: {file} not found!")
        exit(1)

# Docker command to detect the barcode and get its position
docker_command = [
    "docker", "run", "--rm",
    "-v", f"{os.getcwd()}:/app",
    "openjdk:17",
    "java", "-cp",
    f"/app/{javase_jar}:/app/{core_jar}:/app/{jcommander_jar}",
    "com.google.zxing.client.j2se.CommandLineRunner",
    f"/app/{barcode_image}"
]

try:
    # Run the Docker command to get the decoding and position
    result = subprocess.run(docker_command, capture_output=True, text=True, check=True)
    output = result.stdout.strip()
    print("Decoded Output:")
    print(output)
except subprocess.CalledProcessError as e:
    print("Error during decoding:")
    print(e.stderr)
    exit(1)

# Check if the output contains "No barcode found"
if "No barcode found" in output:
    print("\nError: No barcode detected in the image.")
    print("Possible reasons:")
    print("1. The image does not contain a valid PDF417 barcode.")
    print("2. The barcode is not clearly visible or is distorted.")
    print("3. The image quality is poor (e.g., blurry, low resolution, or improper lighting).")
    print("4. The barcode is rotated or skewed.")
    exit(1)

# Parse the ZXing output for barcode position and decoded data
points = []
decoded_data = None

# Extract decoded data
for line in output.splitlines():
    if line.strip().startswith("Raw result:"):
        decoded_data = line.split("Raw result:")[1].strip()
    elif line.strip().startswith("Parsed result:"):
        decoded_data = line.split("Parsed result:")[1].strip()
    elif line.startswith("  Point"):
        parts = line.split(":")[1].strip().replace("(", "").replace(")", "").split(",")
        points.append((int(float(parts[0])), int(float(parts[1]))))

# Print decoded data in human-readable format
if decoded_data:
    print("\nDecoded Information (Human Readable):")
    print(decoded_data)
else:
    print("No decoded data found.")

# If points are found, draw a bounding polygon
if len(points) >= 4:
    # Load the image with OpenCV
    image = cv2.imread(barcode_image)
    if image is None:
        print("Error: Unable to read the image!")
        exit(1)

    # Draw a polygon connecting the points
    points_array = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
    print(f"Drawing polygon with points: {points}")

    cv2.polylines(image, [points_array], isClosed=True, color=(0, 255, 0), thickness=2)

    # Save and display the annotated image
    annotated_image_path = "annotated_barcode.png"
    cv2.imwrite(annotated_image_path, image)
    print(f"Annotated image saved as {annotated_image_path}")

    # Display the image
    cv2.imshow("Detected Barcode", image)
    print("Press any key to close the window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No bounding box points detected.")