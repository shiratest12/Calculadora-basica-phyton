#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter  as think

win = think.Tk()
win.geometry("520x420")
win.configure(background="#BB00FE")
win.title("Calculadora")
show_text = think.StringVar()



#ventana principal
input_frame = think.Frame(win, width=312, height=50, bd=7, highlightbackground="black", background="#45035D", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=think.TOP)
input_field = think.Entry(input_frame, font=('arial', 25), textvariable=show_text, width=50, bg="#F2CEF1", bd=0, justify=think.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=15)
buttons_frame = think.Frame(win, width=312, height=272.5, bg="grey")
buttons_frame.pack()

#botones
#1
button_0 = think.Button(buttons_frame, text="0", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(0))
button_0.grid(row=1, column=0, padx=1, pady=1)
button_1 = think.Button(buttons_frame, text="1", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(1))
button_1.grid(row=1, column=1, padx=1, pady=1)
button_2 = think.Button(buttons_frame, text="2", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(2))
button_2.grid(row=1, column=2, padx=1, pady=1)
button_3 = think.Button(buttons_frame, text="3", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(3))
button_3.grid(row=1, column=3, padx=1, pady=1)

#2
button_4 = think.Button(buttons_frame, text="4", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(4))
button_4.grid(row=2, column=0, padx=1, pady=1)
button_5 = think.Button(buttons_frame, text="5", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(5))
button_5.grid(row=2, column=1, padx=1, pady=1)
button_6 = think.Button(buttons_frame, text="6", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(6))
button_6.grid(row=2, column=2, padx=1, pady=1)
button_7 = think.Button(buttons_frame, text="7", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(7))
button_7.grid(row=2, column=3, padx=1, pady=1)

#3
button_8 = think.Button(buttons_frame, text="8", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(8))
button_8.grid(row=3, column=0, padx=1, pady=1)
button_9 = think.Button(buttons_frame, text="9", fg="black", width=15, height=3, bd=0, bg="#FFE8F4", cursor="hand2", command=lambda: action(9))
button_9.grid(row=3, column=1, padx=1, pady=1)
sumar_button = think.Button(buttons_frame, text="+", fg="black", width=15, height=3, bd=0, bg="#F2CEF1", cursor="hand2", command=lambda: action("+"))
sumar_button.grid(row=3, column=2, padx=1, pady=1)
punto_button = think.Button(buttons_frame, text=".", fg="black", width=15, height=3, bd=0, bg="#F2CEF1", cursor="hand2", command=lambda: action("."))
punto_button.grid(row=3, column=3, padx=1, pady=1)

#4
igual_button = think.Button(buttons_frame, text="=", fg="black", width=15, height=3, bd=0, bg="#F2CEF1", cursor="hand2", command=result)
igual_button.grid(row=4, column=0, padx=1, pady=1)
restar_button = think.Button(buttons_frame, text="-", fg="black", width=15, height=3, bd=0, bg="#F2CEF1", cursor="hand2", command=lambda: action("-"))
restar_button.grid(row=4, column=1, padx=1, pady=1)
multiplicar_button = think.Button(buttons_frame, text="x", fg="black", width=15, height=3, bd=0, bg="#F2CEF1", cursor="hand2", command=lambda: action("*"))
multiplicar_button.grid(row=4, column=2, padx=1, pady=1)
dividir_button = think.Button(buttons_frame, text="/", fg="black", width=15, height=3, bd=0, bg="#F2CEF1", cursor="hand2", command=lambda: action("/"))
dividir_button.grid(row=4, column=3, padx=1, pady=1)

#5

clear_button = think.Button(buttons_frame, text="C", fg="black", width=36, height=5, bd=0, bg="#F2CEF1", cursor="hand2", command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=1, pady=1)

#main
win.mainloop()

def action(item):
    global num
    num = num + str(item)
    show_text.set(num)

def clear():
    global num
    num = ""
    show_text.set("")

def result():
    global num
    result = str(eval(num))
    show_text.set(result)
    num = ""

