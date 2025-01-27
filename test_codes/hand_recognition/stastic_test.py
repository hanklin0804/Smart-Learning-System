import numpy as np
import mediapipe as mp
import PoseTable  
from cv2 import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

start_count = 0
start_x,start_y = 0,0

hands = mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5,max_num_hands = 1)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success,image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue
    
    
    # Flip the image horizontally for a later selfie-view display,Convertx the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    

    # Copy prototype image for cropping image
    image_proto = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    # Draw the hand annotations on the image.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    annotated_image = image.copy()

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)


        # Connect all the finger point
        mp_drawing.draw_landmarks(annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Gesture recognition 
        for hand_landmarks in results.multi_hand_landmarks:
           PoseTable.catching_start(image,image_proto,start_count,start_x,start_y,finger_detected,ROI_x,ROI_y)
        
    
    # Image display
    cv2.imshow('MediaPipe Hands', image)

    if cv2.waitKey(5) & 0xFF == 27 :
        break

hands.close()
cap.release()