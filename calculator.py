import tkinter as tk

# Function to perform calculations
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operator.get()

    if operation == "+":
        result.set(num1 + num2)
    elif operation == "-":
        result.set(num1 - num2)
    elif operation == "*":
        result.set(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Error: Division by zero")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator - Codsoft")

# Entry fields for numbers
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Dropdown for operation selection
operator = tk.StringVar(root)
operator.set("+")  # Default operation is addition
operator_menu = tk.OptionMenu(root, operator, "+", "-", "*", "/")
operator_menu.pack()

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Display the result
result = tk.StringVar(root)
result.set("Result will be shown here")
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Start the tkinter main loop
root.mainloop()
