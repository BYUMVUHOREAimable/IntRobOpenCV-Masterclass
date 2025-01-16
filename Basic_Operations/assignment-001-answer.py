import cv2

def annotate_license_plate(input_path, output_path):
    """
    Annotate an image by adding a bounding box and text for a license plate.
    
    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the annotated image.
        
    Returns:
        Annotated image if successful, None otherwise.
    """
    try:
        # Load the image from the input path
        image = cv2.imread(input_path)
        if image is None:
            raise FileNotFoundError("Could not load the image. Check the file path.")
        
        # Get the dimensions of the image (height and width)
        height, width = image.shape[:2]
        
        # Define coordinates for the license plate bounding box
        x1, y1 = int(width * 0.21), int(height * 0.20)  # Top-left corner of the box
        x2, y2 = int(width * 0.78), int(height * 0.97)  # Bottom-right corner of the box

        # Draw a green rectangular bounding box around the license plate
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 6)  # (BGR color: green, thickness: 6)

        # Define the text for the license plate
        text = "RAH972U"
        text_x, text_y = int(width * 0.68), int(height * 0.19)  # Position of the text
        font = cv2.FONT_HERSHEY_SIMPLEX  # Font type for the text
        font_scale, thickness = 1.5, 4  # Font scale and text thickness
        color = (0, 255, 0)  # Text color (green in BGR format)

        # Calculate the size of the text box
        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
        
        # Create an overlay for the semi-transparent text background
        overlay = image.copy()  # Copy of the original image for overlay
        cv2.rectangle(
            overlay,
            (text_x - 5, text_y - text_height - 5),  # Top-left corner of the background
            (text_x + text_width + 5, text_y + 5),  # Bottom-right corner of the background
            (0, 0, 0),  # Background color (black in BGR)
            -1  # Filled rectangle
        )
        
        # Blend the overlay with the original image to create a semi-transparent effect
        cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

        # Add the license plate text on top of the background
        cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness)

        # Save the annotated image to the specified output path
        cv2.imwrite(output_path, image)

        # Return the annotated image for further use
        return image
    except Exception as e:
        # Print an error message if any exception occurs
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to handle image annotation and display.
    """
    # Specify the input and output image file paths
    input_image = "assignment-001-given.jpg"  # Input image path
    output_image = "assignment-001-result.jpg"  # Output image path to save the result

    # Call the annotate_license_plate function to annotate the image
    result = annotate_license_plate(input_image, output_image)

    if result is not None:
        # Display the annotated image in a window
        cv2.imshow("Annotated License Plate", result)
        print("Press any key to close the image and save the result.")
        
        # Wait for any key press to close the image window
        cv2.waitKey(0)
        cv2.destroyAllWindows()  # Close the display window
        
        # Confirm that the image has been saved
        print(f"Annotated image saved at {output_image}.")
    else:
        # Print a message if the annotation process failed
        print("Failed to annotate the image.")


if __name__ == "__main__":
    # Entry point of the script
    main()
