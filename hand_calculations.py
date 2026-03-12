import cv2
import mediapipe as mp
import pyttsx3
import time

# Voice setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Mediapipe setup
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Count fingers
def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []
    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    for tip in tips[1:]:
        fingers.append(
            1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0
        )
    return sum(fingers)

# Detect operator
def detect_operator(finger_count):
    if finger_count == 1:
        return '+'
    elif finger_count == 2:
        return '-'
    elif finger_count == 3:
        return '*'
    elif finger_count == 4:
        return '/'
    return None

# Speak and print
def say(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Main logic
cap = cv2.VideoCapture(0)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

mode = "choose_operator"
operator = None
operand1 = operand2 = None
start_time = time.time()

say("Show fingers to choose operation. 1 for addition, 2 for subtract, 3 for multiply, 4 for divide.")

while True:
    success, frame = cap.read()
    if not success:
        continue

    image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    finger_counts = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            finger_counts.append(count_fingers(hand_landmarks))

    if mode == "choose_operator" and finger_counts:
        op = detect_operator(finger_counts[0])
        if op:
            operator = op
            say(f"Operator selected: {operator}. Now show first number with fingers.")
            mode = "first_number"
            time.sleep(2)

    elif mode == "first_number" and len(finger_counts) >= 1:
        operand1 = finger_counts[0]
        say(f"First number is {operand1}. Now show second number.")
        mode = "second_number"
        time.sleep(2)

    elif mode == "second_number" and len(finger_counts) >= 1:
        operand2 = finger_counts[0]
        result = 0
        try:
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                result = operand1 / operand2 if operand2 != 0 else "undefined"
        except Exception as e:
            result = f"Error: {str(e)}"

        say(f"Result of {operand1} {operator} {operand2} is {result}")
        mode = "done"

    elif mode == "done":
        say("Press Q to exit or R to restart")
        mode = "wait_key"

    cv2.imshow("Hand Calculator", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('r'):
        operator = None
        operand1 = operand2 = None
        mode = "choose_operator"
        say("Restarting. Show operator with fingers.")

cap.release()
cv2.destroyAllWindows()
