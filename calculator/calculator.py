import tkinter as tk
import math

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def calculate_result(expression):
    try:
        result = eval(expression)  
        return result
    except (SyntaxError, NameError, ZeroDivisionError):
        return "Error"

def evaluate_calculation():
    global calculation
    result = calculate_result(calculation)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, str(result))

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk(className="Calculator")
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

button_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial"))
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial"))
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial"))
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial"))
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial"))
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial"))
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial"))
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial"))
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial"))
button_9.grid(row=4, column=3)
button_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial"))
button_0.grid(row=5, column=2)
button_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial"))
button_plus.grid(row=2, column=4)
button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial"))
button_minus.grid(row=3, column=4)
button_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial"))
button_mult.grid(row=4, column=4)
button_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial"))
button_div.grid(row=5, column=4)
button_p = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial"))
button_p.grid(row=5, column=1)
button_p2 = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial"))
button_p2.grid(row=5, column=3)
button_clear = tk.Button(root, text="C", command=clear_field, width=30, font=("Arial"))
button_clear.grid(row=1, column=1, columnspan=5)
button_equal = tk.Button(root, text="=", command=evaluate_calculation, width=30, font=("Arial"))
button_equal.grid(row=6, column=1, columnspan=5)

root.mainloop()

