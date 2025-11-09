# Simple GUI Calculator using Tkinter
import tkinter as tk

# Create main application window
window = tk.Tk()
window.title("Python Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Entry widget to display expressions
expression = ""

def press(num):
    """Handle button press"""
    global expression
    expression += str(num)
    equation.set(expression)

def clear():
    """Clear the entry screen"""
    global expression
    expression = ""
    equation.set("")

def evaluate():
    """Evaluate the expression and handle errors"""
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except ZeroDivisionError:
        equation.set("Error: Divide by 0")
        expression = ""
    except Exception:
        equation.set("Error")
        expression = ""

# StringVar to track the text entry
equation = tk.StringVar()

# Input field
entry_field = tk.Entry(window, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry_field.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                  bg="lightgreen", command=evaluate).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "C":
        tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                  bg="lightcoral", command=clear).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Run the main GUI loop
window.mainloop()