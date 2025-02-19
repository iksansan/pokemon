import tkinter as tk
import tkinter.messagebox 
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('MUHAMAD IKSAN')

window.attributes('-fullscreen', True)

frame = tk.Frame(master=window, bg="black",padx=10)
frame.pack(fill=tk.BOTH, expand=True)
entry = tk.Entry(master=frame, relief=SUNKEN,
 borderwidth=10, font=('arial', 40, ),fg='lightgreen',bg='black', width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2, sticky="nsew")

def myclick(number):
    entry.insert(tk.END,number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error")

def comma():
    current = entry.get()
    if current == "":
        entry.insert(tk.END, '0,')
    elif current[-1] != ',':
        entry.insert(tk.END, ',')

def percentage():
    current = entry.get()
    try:
        result = eval(current.replace(',', '.')) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def equal():
    try:
        result = eval(entry.get().replace(',', '.').replace('^',''))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

def delete_last():
    current_value = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_value[:-1])


button_1 =tk.Button(master=frame, text='7', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(7))
button_1.grid(row=2, column=0, pady=2, sticky="nsew")

button_2 =tk.Button(master=frame, text='8', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(8))
button_2.grid(row=2, column=1, pady=2, sticky="nsew")

button_3 =tk.Button(master=frame, text='9', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(9))
button_3.grid(row=2, column=2, pady=2, sticky="nsew")

button_3 =tk.Button(master=frame, text='4', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(4))
button_3.grid(row=3, column=0, pady=2, sticky="nsew")

button_4 =tk.Button(master=frame, text='5', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(5))
button_4.grid(row=3, column=1, pady=2, sticky="nsew")

button_5 =tk.Button(master=frame, text='6', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(6))
button_5.grid(row=3, column=2, pady=2, sticky="nsew")

button_6 =tk.Button(master=frame, text='1', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(1))
button_6.grid(row=4, column=0, pady=2, sticky="nsew")

button_7 =tk.Button(master=frame, text='2', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(2))
button_7.grid(row=4, column=1, pady=2, sticky="nsew")

button_8 =tk.Button(master=frame, text='3', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(3))
button_8.grid(row=4, column=2, pady=2, sticky="nsew")

button_9 =tk.Button(master=frame, text='0', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick(0))
button_9.grid(row=5, column=1, pady=2, sticky="nsew")

#vfswf

button_clear = tk.Button(master=frame, text='C', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,fg="red",
 command=clear)
button_clear.grid(row=1, column=0, columnspan=1, pady=1, sticky="nsew")

button_percentage = tk.Button(master=frame, text="%", padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=percentage)
button_percentage.grid(row=1, column=1, pady=1, sticky="nsew")

button_delete = tk.Button(master=frame, text='DEL', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,fg="red",
 command=delete_last)
button_delete.grid(row=1, column=2, columnspan=1, pady=1, sticky="nsew")

button_div = tk.Button (master=frame, text="÷", padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick('/'))
button_div.grid(row=1, column=3, pady=1, sticky="nsew")

button_multiply = tk.Button (master=frame, text="x", padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick('*'))
button_multiply.grid(row=2, column=3, pady=1, sticky="nsew")

button_subtract = tk.Button (master=frame, text="-", padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick('-'))
button_subtract.grid(row=3, column=3, pady=1, sticky="nsew")

button_add = tk.Button (master=frame, text="+", padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=lambda:myclick('+'))
button_add.grid(row=4, column=3, pady=1, sticky="nsew")

button_equal = tk.Button(master=frame, text='=', padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,fg="red",
 command=equal)
button_equal.grid(row=5, column=3, columnspan=2, pady=1, sticky="nsew")

button_comma = tk.Button(master=frame, text=",", padx=15, borderwidth=10, pady=5, bg="grey", font=('arial', 30), width=3,
 command=comma)
button_comma.grid(row=5, column=2, pady=1, sticky="nsew")

button_pangkat = tk.Button(master=frame, text="^", padx=15, pady=5,bg="grey", borderwidth=10,font=('arial',25), width=3,
 command=lambda: myclick('^'))
button_pangkat.grid(row=5, column=0, pady=2, sticky="nsew")


for i in range(8):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)


def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)


window.bind('<Escape>', end_fullscreen)

window.mainloop()







