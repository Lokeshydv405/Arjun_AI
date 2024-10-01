import cv2
import mediapipe as mp

class PostureDetector:
    def __init__(self):
        # Initialize MediaPipe Pose.
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

        # Initialize MediaPipe drawing.
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_posture(self, frame):
        # Convert the BGR image to RGB.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image and detect the pose.
        results = self.pose.process(rgb_frame)

        # Draw the pose annotation on the image.
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
            for ld, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
                cv2.putText(frame, str(ld), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        return frame, results
    
    def get_body_part_positions(self, results):
        body_parts = {
            'left_hand': [15, 17, 19, 21],
            'right_hand': [16, 18, 20, 22],
            'chest': [11, 12],
            'face': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'eyes': [1, 2],
            'legs': [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
        }
        
        positions = {part: [] for part in body_parts}
        
        if results.pose_landmarks:
            for part, indices in body_parts.items():
                for idx in indices:
                    lm = results.pose_landmarks.landmark[idx]
                    positions[part].append((lm.x, lm.y, lm.z))
        
        return positions
    
def main():
    detector = PostureDetector()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detector.detect_posture(frame)

        # Display the frame.
        cv2.imshow('Posture Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()