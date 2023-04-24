import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('500x550')
root.resizable(False, False)
root.configure(bg='#1c3169')


# Logic
def calc(operation):
     global number

     if operation == 'AC':
         number = '0'

     elif operation == '=':
         number = str(eval(number))

     elif operation == '+/-':
         number = '-'

     elif operation == 'del':
         number = number[0: -1]

     elif operation == '%':
         number = str(eval(number) / 100)

     else:
         if number == '0':
             number = ''

         number += operation
     label.configure(text=number)

number = '0'
label = tk.Label(text=number, font=('Myriad Pro', 35), bg='#1c3169', fg='white')
label.place(x=20, y=50)

# Create buttons
btns = [
    'AC', 'del', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', ',', '+/-', '='
]
x = 18
y = 140
for btn in btns:
    get_lbl = lambda x=btn: calc(x)
    tk.Button(text=btn, bg='#2cb327', font=('Myriad Pro', 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81
root.mainloop()