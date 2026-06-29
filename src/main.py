import cv2
import mediapipe as mp
import numpy as np

# Load Images
thumb_img = cv2.imread('../assets/Thumb.jpg')
peace_img = cv2.imread('../assets/Peace.jpg')
screaming_img = cv2.imread('../assets/Screaming.jpg')
happy_img = cv2.imread('../assets/Happy.jpg')

thumb_img = cv2.resize(thumb_img, (300, 300))
peace_img = cv2.resize(peace_img, (300, 300))
screaming_img = cv2.resize(screaming_img, (300, 300))
happy_img = cv2.resize(happy_img, (300, 300))
blank = np.zeros((300, 300, 3), dtype=np.uint8)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def get_finger_states(lm):
    fingers = []
    fingers.append(lm[4].x > lm[3].x)
    fingers.append(lm[8].y < lm[6].y)
    fingers.append(lm[12].y < lm[10].y)
    fingers.append(lm[16].y < lm[14].y)
    fingers.append(lm[20].y < lm[18].y)
    return fingers

def classify_gesture(fingers):
    if fingers[0] and not any(fingers[1:]):
        return "THUMB"
    if fingers[1] and fingers[2] and not fingers[3] and not fingers[4]:
        return "PEACE"
    if not any(fingers):
        return "SCREAMING"
    if all(fingers):
        return "HAPPY"
    return "NONE"

cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
cv2.namedWindow("Meme", cv2.WINDOW_NORMAL)

cv2.moveWindow("Camera",0,0)
cv2.moveWindow("Meme", 650, 0)

current_meme = blank.copy()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    gesture = "NONE"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark
            fingers = get_finger_states(lm)
            gesture = classify_gesture(fingers)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if gesture == "THUMB":
        current_meme = thumb_img
    elif gesture == "PEACE":
        current_meme = peace_img
    elif gesture == "SCREAMING":
        current_meme = screaming_img
    elif gesture == "HAPPY":
        current_meme = happy_img
    else:
        current_meme = blank.copy()
        cv2.putText(current_meme, "Please show a gesture", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255),2)
    
    cv2.imshow("Camera", frame)
    cv2.imshow("Meme", current_meme)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()