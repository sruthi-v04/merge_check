import cv2
import numpy as np

# Load and preprocess the image
image = cv2.imread(r"C:\Users\sruth\Desktop\processed_images\05-07-2022_1-XRayTest.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

def contour_iou(contour1, contour2):
    # Create bounding rectangles for the contours
    x1, y1, w1, h1 = cv2.boundingRect(contour1)
    x2, y2, w2, h2 = cv2.boundingRect(contour2)
    
    # Calculate intersection
    xi1, yi1 = max(x1, x2), max(y1, y2)
    xi2, yi2 = min(x1+w1, x2+w2), min(y1+h1, y2+h2)
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    
    # Calculate union
    box1_area = w1 * h1
    box2_area = w2 * h2
    union_area = box1_area + box2_area - inter_area
    
    # Calculate Intersection over Union (IoU)
    iou = inter_area / union_area
    return iou

def check_if_texts_merged(contours):
    for i in range(len(contours)):
        for j in range(i + 1, len(contours)):
            # Calculate IoU for contours[i] and contours[j]
            if contour_iou(contours[i], contours[j]) > 0.5:
                return True
    return False

merged = check_if_texts_merged(contours)
print("Texts are merged" if merged else "Texts are separate")

# Optional: Visualize contours
image_contours = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
cv2.imshow('Contours', image_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
