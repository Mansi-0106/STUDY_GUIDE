import cv2
import dlib
from scipy.spatial import distance
import numpy as np

# define eye aspect ratio function
def eye_aspect_ratio(eye):
    # compute distances between landmarks
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    # compute eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

# initialize detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\mansi\OneDrive\Desktop\DROWSINESS DETECTION\shape_predictor_68_face_landmarks.dat")

# initialize camera
cap = cv2.VideoCapture(0)

while True:
    # read frame from camera
    ret, frame = cap.read()
    
    # convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # detect faces in grayscale image
    faces = detector(gray, 0)
    
    # check if any faces are detected
    if len(faces) == 0:
        cv2.putText(frame, "Distracted", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # loop over detected faces
    for face in faces:
        # predict facial landmarks
        landmarks = predictor(gray, face)
        landmarks = [[landmarks.part(i).x, landmarks.part(i).y] for i in range(68)]
        landmarks = np.array(landmarks, dtype=np.int32)

        # extract eye landmarks
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]

        # compute eye aspect ratios
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        ear = (left_ear + right_ear) / 2.0

        # draw eyes on frame
        cv2.polylines(frame, [left_eye], True, (0, 255, 0), 2)
        cv2.polylines(frame, [right_eye], True, (0, 255, 0), 2)

        # check if eyes are closed
        if ear < 0.2:
            cv2.putText(frame, "Distracted", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Focus", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # handle case where eyes are not detected
        if len(left_eye) == 0 or len(right_eye) == 0:
            cv2.putText(frame, "Distracted", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
    # display frame
    cv2.imshow("Camera Feed", frame)
    
    # exit program when "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release camera and close window
cap.release()
cv2.destroyAllWindows()
