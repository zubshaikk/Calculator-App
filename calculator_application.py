import tkinter as tk

def press(num):
    global equation_txt
    equation_txt = equation_txt + str(num)
    equation_label.set(equation_txt)

def answer():
    global equation_txt
    try:    
        total = str(eval(equation_txt))
        equation_label.set(total)
        equation_txt = total
    except ZeroDivisionError:
        equation_label.set('Undefined')
    except SyntaxError:
        equation_label.set('Syntax error')
def clear():
    global equation_txt
    equation_label.set("")
    equation_txt = ""

window = tk.Tk()

window.title("Calculator Application")
window.geometry("500x500")

equation_txt = ""
equation_label = tk.StringVar()

label = tk.Label(window, textvariable=equation_label, font=20, bg="white", width=24, height=2)
label.pack()

#Frame creation to place all buttons
frame = tk.Frame(window)
frame.pack()

#1-9 Buttons Creation
buttons = [[tk.Button(frame, text=str(j + i * 3), height=4, width=9, font=35, 
                      command=lambda num=j + i * 3: press(num)) for j in range(1, 4) ] for i in range(3)]

#1-9 Buttons Placement 
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)
        
#0 Button Creation and Placement
button0 = tk.Button(frame, text="0", height=4, width=9, font=35, command=lambda: press(0))
button0.grid(row=3, column=1)

#Plus Button Creation and Placement
button_plus = tk.Button(frame, text='+', height=4, width=9, font=35, command=lambda: press('+'))
button_plus.grid(row=0, column=3)


#Minus Button Creation and Placement
button_minus = tk.Button(frame, text='-', height=4, width=9, font=35, command=lambda: press('-'))
button_minus.grid(row=1, column=3)

#Multiplication Button Creation and Placement
button_multiply = tk.Button(frame, text='*', height=4, width=9, font=35, command=lambda: press('*'))
button_multiply.grid(row=2, column=3)

#Division Button Creation and Placement
button_divide = tk.Button(frame, text='/', height=4, width=9, font=35, command=lambda: press('/'))
button_divide.grid(row=3, column=3)

#Equal Button Creation and Placement
button_equal = tk.Button(frame, text='=', height=4, width=9, font=35, command=answer)
button_equal.grid(row=3, column=2)

#Decimal Button Creation and Placement
button_decimal = tk.Button(frame, text='.', height=4, width=9, font=35, command=lambda: press('.'))
button_decimal.grid(row=3, column=0)

#Clear Button Creation and Placement
button_clear = tk.Button(window, text='Clear', height=4, width=19, font=35, command=clear)
button_clear.pack()

#Keep the window Open
window.mainloop()
