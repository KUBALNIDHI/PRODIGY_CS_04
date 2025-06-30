# ⌨️🛡️ Simple Keylogger
This program is a basic keylogger that records and logs keystrokes along with timestamps, saving them to a file for learning and demonstration purposes in cybersecurity education.

__________

# 🧠  Features
✅ Records keystrokes in real-time.

✅ Adds timestamps for each keystroke for tracking practice.

✅ Stops cleanly when Esc is pressed.

✅ Lightweight and easy to understand for beginners.

✅ Suitable for demonstrating ethical monitoring concepts in cybersecurity.

______________

# 🛠️ Requirements
Python 3.x

pynput library

_______


# ⚙️ How It Works
🔹 Listens for keyboard key press events using the pynput library.

🔹 Captures the key pressed and the current timestamp.

🔹 Logs this information into key_log.txt.

🔹 Stops recording when the Esc key is pressed.

________

# 💻 How to Run
1. **Clone this repository**
2. **Run the script**:
   ```bash
   python keylogger.py
3. **Start typing; keys will be logged in key_log.txt.**  
4. **Press Esc to stop logging safely.**
