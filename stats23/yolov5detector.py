import cv2
import torch
import numpy as np
from time import time
import argparse

def list_available_cameras():
    """List available camera indices by trying to open each one."""
    available_cameras = []
    # Try camera indices 0-9 (adjust range as needed)
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, _ = cap.read()
            if ret:
                available_cameras.append(i)
                print(f"Camera {i} is available")
            cap.release()
    return available_cameras

def select_camera():
    """Interactive camera selection."""
    available_cameras = list_available_cameras()
    
    if not available_cameras:
        print("No cameras detected!")
        return None
    
    print("\nAvailable cameras:")
    for idx in available_cameras:
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print(f"Camera {idx}: {width}x{height}")
        cap.release()
    
    while True:
        try:
            selection = int(input("\nSelect camera index (or -1 to exit): "))
            if selection == -1:
                return None
            if selection in available_cameras:
                return selection
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def run_detection(camera_index=None):
    """Run YOLOv5 person detection on the selected camera."""
    # If no camera index specified, prompt for selection
    if camera_index is None:
        camera_index = select_camera()
        if camera_index is None:
            print("Camera selection cancelled.")
            return
    
    print(f"Starting detection with camera {camera_index}...")
    
    # Load YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    
    # Configure to detect only people (class 0 in COCO dataset)
    model.classes = [0]  # 0 is the index for 'person'
    
    # Configure video capture
    cap = cv2.VideoCapture(camera_index)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index}")
        return
    
    # Configure parameters
    frame_count = 0
    start_time = time()
    fps = 0
    
    while True:
        # Capture frame
        ret, frame = cap.read()
        if not ret:
            print("Error capturing frame")
            break
        
        # Perform detection
        results = model(frame)
        
        # Get detection information
        detections = results.pandas().xyxy[0]  # Results in pandas format
        
        # Draw bounding boxes
        for i, detection in detections.iterrows():
            x1, y1, x2, y2 = int(detection['xmin']), int(detection['ymin']), int(detection['xmax']), int(detection['ymax'])
            conf = detection['confidence']
            label = f"Person: {conf:.2f}"
            
            # Draw rectangle and text
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Calculate and display FPS
        frame_count += 1
        if (time() - start_time) > 1:
            fps = frame_count / (time() - start_time)
            frame_count = 0
            start_time = time()
        
        fps_text = f"FPS: {fps:.2f}"
        cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Show number of people detected
        num_persons = len(detections)
        persons_text = f"People detected: {num_persons}"
        cv2.putText(frame, persons_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Camera information
        camera_text = f"Camera: {camera_index}"
        cv2.putText(frame, camera_text, (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Show result
        cv2.imshow('YOLOv5 Person Detection', frame)
        
        # Exit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YOLOv5 Person Detection')
    parser.add_argument('--camera', type=int, help='Camera index to use')
    args = parser.parse_args()
    
    run_detection(args.camera)