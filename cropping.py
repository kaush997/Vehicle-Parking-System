import cv2
from ultralytics import YOLO

# Load license plate detector model
license_plate_detector = YOLO('license_plate_detector.pt')

# Load image
image = cv2.imread('Resources/12.jpg')

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
    cv2.imwrite(f'croppedImages/cropped_plate_{cropped_image_counter}.png', license_plate_crop)

    # Increment counter for next image
    cropped_image_counter += 1
