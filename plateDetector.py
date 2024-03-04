import cv2
import os

# Define the name of the image file
vehicle_image = "12.jpg"

# Get the current working directory
cwd = os.getcwd()

# Construct the path to the image file
image_path = os.path.join(cwd, "resources", vehicle_image)

# Print the path to the image file
print("Path to the image file:", image_path)

# Load image from path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    print("Image loaded successfully.")

    # Resize image
    desired_width = 533  # Specify desired width
    desired_height = 710  # Specify desired height
    resized_image = cv2.resize(image, (desired_width, desired_height))

    # Define the angle of rotation (in degrees)
    angle = -5

    # Calculate the center of the image
    center = (resized_image.shape[1] // 2, resized_image.shape[0] // 2)

    # Generate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply the rotation transformation to the image
    rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (resized_image.shape[1], resized_image.shape[0]))

    # Display the resized image
    cv2.imshow("Rotated_image", rotated_image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed to load image. Please check the file path.")
