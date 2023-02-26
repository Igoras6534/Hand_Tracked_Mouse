import cv2 
import mediapipe as mp
import pyautogui


cam=cv2.VideoCapture(1) # Choose your webcam
mpHands=mp.solutions.hands
hands=mpHands.Hands()


def tracking(hand_LMS): #Use your pointing finger to tracke the mouse
    for id, lm in enumerate(hand_LMS.landmark):
        for id, lm in enumerate(hand_LMS.landmark):
            if id==8:
                cx,cy=int(lm.x*1920),int(lm.y*1080) #Adjust with your resolution
                pyautogui.moveTo(cx,cy)    

def clicking(hand_LMS): #Touch your thumb with a pointing finger to click 
    click_data=[hand_LMS.landmark[4],hand_LMS.landmark[8]]
    if click_data[0].x - click_data[1].x <0.018 and  click_data[0].y - click_data[1].y<0.023:
        pyautogui.click()
while True:
    success,frame=cam.read()
    frame=cv2.flip(frame,1)
    frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    if results.multi_hand_landmarks:
        for hand_LMS in results.multi_hand_landmarks:
            tracking(hand_LMS)                
            clicking(hand_LMS)           
    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
# It is better to use high fps rate webcam