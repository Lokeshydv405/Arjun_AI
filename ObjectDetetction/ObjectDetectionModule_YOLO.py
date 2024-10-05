import cv2
from ultralytics import YOLO
import cvzone
import math

class YoloWithWebcam:
    def __init__(self, camera_index=0, model_path="../Yolo_Weights/yolov8l.pt",frame = None):
        self.cap = cv2.VideoCapture(camera_index)
        self.frame = frame
        self.model = YOLO(model_path)
        self.cap.set(6, 720)
        self.classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                           "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                           "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
                           "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
                           "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                           "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
                           "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
                           "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
                           "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                           "teddy bear", "hair drier", "toothbrush"]

    def run(self):
        while True:
            if self.frame is not None:
                img = self.frame
                ret = True
            else:
                ret, img = self.cap.read()
            if not ret:
                print("Failed to capture image")
                break

            results = self.model(img, stream=True)
            for r in results:
                print(r)
                boxes = r.boxes
                for box in boxes:
                    # box Identification
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    w, h = x2 - x1, y2 - y1
                    cvzone.cornerRect(img, (x1, y1, w, h))

                    # confidence Level
                    conf = math.ceil(box.conf[0] * 100)
                    # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),3)

                    # Class Name
                    cls = int(box.cls[0])
                    cvzone.putTextRect(img, f"{self.classNames[cls]} {conf / 100}", (max(0, x1), max(35, y1)))
            return img
        #     cv2.imshow("Image", img)
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break

        # self.cap.release()
        # cv2.destroyAllWindows()
        
    def detect_objects(self, img):
        results = self.model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Get bounding box coordinates
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))

                # Get the confidence level
                conf = math.ceil(box.conf[0] * 100)

                # Get the class name
                cls = int(box.cls[0])
                cvzone.putTextRect(img, f"{self.classNames[cls]} {conf / 100}", (max(0, x1), max(35, y1)))
        return img 
    
def main():
    yolo_webcam = YoloWithWebcam()
    yolo_webcam.run() 
if __name__ == "__main__":
    yolo_webcam = YoloWithWebcam()
    yolo_webcam.run()
