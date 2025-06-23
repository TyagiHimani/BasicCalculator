# 🧮 Simple Calculator

**Author:** Himani Tyagi  
**Internship Project Submission**

---

## 📌 Description

This is a basic console-based calculator developed in Python that performs fundamental arithmetic operations: addition, subtraction, multiplication, and division. It takes user input, handles invalid entries gracefully, and supports continuous calculation until the user decides to exit.

---

## 💡 Features

- ✅ Supports four basic operations: `+`, `-`, `*`, `/`
- ✅ Accepts both number-based (`1/2/3/4`) and symbol-based input (`+/-/*//`)
- ✅ Handles invalid numeric input using `try-except`
- ✅ Checks for division by zero with appropriate error message
- ✅ User-friendly interface with looped operations until exit
- ✅ Includes short time delays for better interaction experience

---

## ⚙️ Technologies Used

- Python 3
- `time` module for creating simple delays
- CLI (Command Line Interface)

---

## 🧠 Code Structure

| File        | Purpose |
|-------------|---------|
| `calculator.py` | Main script containing all functions and logic |

**Functions Explained:**

- `add(x, y)` – Returns the sum of `x` and `y`
- `subtract(x, y)` – Returns the difference of `x` and `y`
- `multiply(x, y)` – Returns the product of `x` and `y`
- `divide(x, y)` – Returns the quotient; checks for division by zero
- `calculator()` – Handles UI, user input, function calls, and error handling

---

## 🧪 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone the repository or download the file.
3. Run the script in terminal or any Python IDE:

```bash
python calculator.py
🚀 Future Improvements
Add support for exponentiation and modulus

GUI-based version using Tkinter or PyQt

Store calculation history

Unit testing for each function

🙋‍♀️ My Contribution
As part of my internship, I independently developed this calculator to strengthen my Python fundamentals. I applied function decomposition, input validation, and loop control, while ensuring user-friendly interaction.

📄 License
This project is licensed under the MIT License.
