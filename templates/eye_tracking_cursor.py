import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
cap = cv2.VideoCapture(0)

screen_w, screen_h = pyautogui.size()

def euclidean_dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def eye_aspect_ratio(landmarks, top, bottom, left, right):
    """Rough measure of how open the eye is"""
    vertical = euclidean_dist(landmarks[top], landmarks[bottom])
    horizontal = euclidean_dist(landmarks[left], landmarks[right])
    return vertical / horizontal if horizontal != 0 else 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # Iris centers
        left_iris = landmarks[473]
        right_iris = landmarks[468]

        eye_x = (left_iris.x + right_iris.x) / 2
        eye_y = (left_iris.y + right_iris.y) / 2

        # Move cursor
        x = int(eye_x * screen_w)
        y = int(eye_y * screen_h)
        pyautogui.moveTo(x, y)

        # Blink detection (using left eye)
        ear = eye_aspect_ratio(
            landmarks,
            top=159, bottom=145,
            left=133, right=33
        )

        # If ratio is small, eye is closed
        if ear < 0.25:  # tweak threshold if needed
            pyautogui.click()
            cv2.putText(frame, "CLICK!", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("Eye Tracking Cursor", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
