# 🖐️ AI Hand Gesture Calculator

A **real-time computer vision based calculator** that performs arithmetic operations using hand gestures.
Built using **Python, OpenCV, and MediaPipe**.

The system detects fingers using a webcam and interprets gestures to perform mathematical operations with optional **voice feedback**.

---

# 🚀 Features

* ✋ Real-time hand detection using **MediaPipe**
* 🔢 Finger counting logic
* ➕ Gesture-based operator selection

| Fingers | Operation      |
| ------- | -------------- |
| 1       | Addition       |
| 2       | Subtraction    |
| 3       | Multiplication |
| 4       | Division       |

* 🎤 Voice feedback using **pyttsx3**
* 👥 Two-hand number detection
* 🔄 Restart and exit controls

---

# 🛠 Tech Stack

* **Python**
* **OpenCV**
* **MediaPipe**
* **pyttsx3** (Text-to-Speech)

---

# 📂 Project Structure

```
AI-Hand-Gesture-Calculator
│
├── hand_calculations.py
├── hand_gesture.py
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Aditya0850/AI-Hand-Gesture-Calculator.git
cd AI-Hand-Gesture-Calculator
```

Install dependencies

```bash
pip install opencv-python mediapipe pyttsx3
```

Run the program

```bash
python hand_calculations.py
```

---

# 🧠 How It Works

1. MediaPipe detects **21 hand landmarks** from the webcam feed.
2. Finger tips are compared with their lower joints to determine whether a finger is raised.
3. The number of raised fingers is mapped to:

   * Mathematical operators
   * Numerical operands
4. The result is displayed on screen and optionally spoken using **text-to-speech**.

---

# 📌 Future Improvements

* Support larger numbers
* Custom gesture recognition
* GUI interface
* More mathematical operations
* Machine learning based gesture classification

---

# 👨‍💻 Author

**Aditya Tiwari**
B.Tech CSE Student

GitHub:
[https://github.com/Aditya0850](https://github.com/Aditya0850)



If you want, I can also show you **3 small changes that will make this project look like a senior-level AI project on GitHub** (takes 15 minutes but makes it much more impressive).
