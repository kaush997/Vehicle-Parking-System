import os
import cv2
from ultralytics import YOLO

# Load license plate detector model
license_plate_detector = YOLO('license_plate_detector.pt')

# Directory paths
input_dir = 'Resources'
output_dir = 'croppedImages'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of image files in the input directory
image_files = [file for file in os.listdir(input_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Loop through each image file
for image_file in image_files:
    # Load image
    image_path = os.path.join(input_dir, image_file)
    image = cv2.imread(image_path)

    # Detect license plates
    license_plates = license_plate_detector(image)[0]

    # Initialize counter for cropped images
    cropped_image_counter = 0

    # Loop through detected license plates
    for license_plate in license_plates.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = license_plate

        # Crop license plate
        license_plate_crop = image[int(y1):int(y2), int(x1): int(x2), :]

        # Save cropped license plate image
        output_path = os.path.join(output_dir, f'{image_file[:-4]}_cropped_{cropped_image_counter}.png')
        cv2.imwrite(output_path, license_plate_crop)

        # Increment counter for next image
        cropped_image_counter += 1
