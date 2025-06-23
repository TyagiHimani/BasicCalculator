# ✊🖐✌ Rock Paper Scissors - Interactive Game

**Author:** Himani Tyagi  
**Internship Project Submission**

---

## 📌 Description

This is a terminal-based **Rock Paper Scissors game** written in Python. It allows a player to enter their name, play multiple rounds against the computer, view live scores, and optionally save their final score to a text file. The game includes basic input validation, randomization for computer moves, and simple interactivity with time delays.

---

## 💡 Features

- 🎮 Interactive CLI gameplay with name personalization
- 🔁 Multiple rounds with option to replay or exit
- 📊 Scoreboard displayed on request
- 🧠 Computer plays with random logic (non-repeating same move)
- 💾 Option to **save your score** to a text file (`scoreboard.txt`)
- ⚠️ Handles invalid inputs and prevents common bugs (e.g. same choices)

---

## ⚙️ Technologies Used

- **Python 3**
- `random` module – for generating computer choices
- `time` module – for delay and smooth user experience
- `file handling` – to store scores persistently

---

## 🧠 Code Structure

| File            | Purpose                              |
|------------------|--------------------------------------|
| `rps_game.py`    | Main script to run the full game     |
| `scoreboard.txt` | (Optional) Stores saved scores       |

### Key Components:

- `name = input(...)` – Gets user’s name at the beginning
- `while True:` – Loops the game for multiple rounds
- `random.randint(1, 3)` – Generates computer move
- `if result == 'player'` – Increases score accordingly
- `open('scoreboard.txt', 'a')` – Appends the final score if user chooses to save

---

## 🧪 How to Run

1. Make sure you have **Python 3 installed**.
2. Save the file as `rps_game.py`
3. Open terminal and run:

```bash
python rps_game.py

🙋‍♀️ My Contribution
This project was created from scratch by me as a part of my internship learning experience. It helped me strengthen core Python skills such as:

Control flow

Functions and logic

File handling

Randomization

User interaction via CLI

📄 License
This project is free to use under the MIT License.
