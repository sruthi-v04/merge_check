import cv2
import numpy as np

# Function to calculate IoU between two bounding boxes
def calculate_iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[0] + boxA[2], boxB[0] + boxB[2])
    yB = min(boxA[1] + boxA[3], boxB[1] + boxB[3])

    # Compute the area of intersection
    interArea = max(0, xB - xA) * max(0, yB - yA)

    # Compute the area of both bounding boxes
    boxAArea = boxA[2] * boxA[3]
    boxBArea = boxB[2] * boxB[3]

    # Compute the IoU
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou

# Function to process image and calculate IoU for each pair of contours
def process_image(image_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Threshold the image
    _, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get bounding boxes for contours
    bounding_boxes = [cv2.boundingRect(c) for c in contours]

    # Calculate IoU for each pair of bounding boxes
    iou_scores = []
    for i in range(len(bounding_boxes)):
        for j in range(i + 1, len(bounding_boxes)):
            iou = calculate_iou(bounding_boxes[i], bounding_boxes[j])
            iou_scores.append(iou)

    return np.mean(iou_scores) if iou_scores else 0

# Paths to the images
left_image_path = r"C:\Users\sruth\Desktop\bounded_after_prep\filtered_images\merged_region_0.png"
right_image_path = r"C:\Users\sruth\Desktop\bounded_after_prep\merged\merged_region_4.png"

# Process both images
left_iou = process_image(left_image_path)
right_iou = process_image(right_image_path)

print(f"Left Image IoU: {left_iou}")
print(f"Right Image IoU: {right_iou}")
