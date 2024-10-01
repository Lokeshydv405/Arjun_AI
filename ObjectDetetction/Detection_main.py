from ObjectDetectionModule_YOLO import YoloWithWebcam
from Posture_detection import PostureDetector
import cv2

def main():
    detector = PostureDetector()
    yolo_webcam = YoloWithWebcam()  # Initialize YOLO only once
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform posture detection
        frame2, results = detector.detect_posture(frame)

        # Perform object detection
        frame3 = yolo_webcam.detect_objects(frame2)  # Use detect_objects method

        # Display the frame with both detections
        cv2.imshow('Posture Detection & YOLO', frame3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
