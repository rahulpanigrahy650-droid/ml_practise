import tkinter as tk

# Function to update the expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

expression = ""
equation = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=equation, font=("Arial",18), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
tk.Button(root, text='7', width=7, height=2, command=lambda: press(7)).grid(row=1, column=0)
tk.Button(root, text='8', width=7, height=2, command=lambda: press(8)).grid(row=1, column=1)
tk.Button(root, text='9', width=7, height=2, command=lambda: press(9)).grid(row=1, column=2)
tk.Button(root, text='/', width=7, height=2, command=lambda: press('/')).grid(row=1, column=3)

tk.Button(root, text='4', width=7, height=2, command=lambda: press(4)).grid(row=2, column=0)
tk.Button(root, text='5', width=7, height=2, command=lambda: press(5)).grid(row=2, column=1)
tk.Button(root, text='6', width=7, height=2, command=lambda: press(6)).grid(row=2, column=2)
tk.Button(root, text='*', width=7, height=2, command=lambda: press('*')).grid(row=2, column=3)

tk.Button(root, text='1', width=7, height=2, command=lambda: press(1)).grid(row=3, column=0)
tk.Button(root, text='2', width=7, height=2, command=lambda: press(2)).grid(row=3, column=1)
tk.Button(root, text='3', width=7, height=2, command=lambda: press(3)).grid(row=3, column=2)
tk.Button(root, text='-', width=7, height=2, command=lambda: press('-')).grid(row=3, column=3)

tk.Button(root, text='0', width=7, height=2, command=lambda: press(0)).grid(row=4, column=0)
tk.Button(root, text='C', width=7, height=2, command=clear).grid(row=4, column=1)
tk.Button(root, text='=', width=7, height=2, command=equalpress).grid(row=4, column=2)
tk.Button(root, text='+', width=7, height=2, command=lambda: press('+')).grid(row=4, column=3)

root.mainloop()