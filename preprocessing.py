import os
import cv2

# Directory paths
input_dir = 'croppedImages'
output_dir = 'preprocessedImages'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

    # Get list of image files in the input directory
    cropped_image_files = [file for file in os.listdir(input_dir) if file.lower().endswith(('.png',))]

    # Loop through each image file
    for cropped_image_file in cropped_image_files:
        # Load image
        image_path = os.path.join(input_dir, cropped_image_file)
        image = cv2.imread(image_path)

        # preprocessing
        #license_plates

        # Initialize counter for preprocessed images
        cropped_image_counter = 0

        # Loop through preprocessed license plates
        for preprocessed_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = preprocessed_plate

            # gdshfsj
            # license_plate_crop

            # Save cropped license plate image
            output_path = os.path.join(output_dir, f'{cropped_image_file[:-4]}_cropped_{cropped_image_counter}.png')
            cv2.imwrite(output_path, license_plate_crop)

            # Increment counter for next image
            cropped_image_counter += 1