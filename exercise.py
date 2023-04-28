import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
s_w, s_h = pyautogui.size()
while True:
    _, frame= cam.read()
    frame=cv2.flip(frame,1) 
    frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    op=face_mesh.process(frame_rgb)
    l_pts=op.multi_face_landmarks
    f_h, f_w, _ = frame.shape
    if l_pts:
        l=l_pts[0].landmark
        for id, landmark in enumerate(l[474:478]):
            x=int(landmark.x * f_w)
            y=int(landmark.y * f_h)
            cv2.circle(frame,(x, y), 3,(0, 255, 0))
            if id == 1:
                s_x=s_w / f_w * x
                s_y=s_h / f_h * y
                pyautogui.moveTo(s_x,s_y)
        left=[l[145], l[159]]
        for landmark in left:
            x = int(landmark.x *f_w)
            y = int(landmark.y *f_h)
            cv2.circle(frame,(x, y), 3,(0, 255, 255))
        if(left[0].y - left[1].y)<0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Exercise',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break