# Pre-Check for Merged Text Segments Using IoU

## Overview
This repository provides a **pre-check mechanism** to verify whether detected text segments in X-Ray images are **merged or distinct** before performing OCR. By analyzing the overlap between bounding boxes using **Intersection over Union (IoU)**, the system determines whether further processing is needed.

## Key Features
- **Contour Detection**: Identifies text-like regions in images using edge detection and bounding box extraction.
- **IoU Calculation**: Computes IoU scores between bounding boxes to measure overlap.
- **Merging Check**: Flags merged regions based on IoU thresholds, preventing unnecessary OCR processing.
- **Bounding Box Visualization**: Displays bounding boxes around detected text regions for validation.

## Workflow
1. **Contour Detection**:
   - Detects potential text regions using edge detection (Canny) and binary thresholding.
   - Extracts bounding boxes for detected regions.
2. **IoU Calculation**:
   - Computes IoU scores for each pair of bounding boxes.
   - Determines if segments are merged based on the overlap score.
3. **Pre-Check Decision**:
   - **Merged Regions**: If IoU is high, OCR is skipped to avoid processing incomplete text segmentation.
   - **Distinct Regions**: If IoU is low, the regions are ready for OCR.


