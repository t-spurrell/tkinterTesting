from tkinter import *

window = Tk()

window.title('MY CALCULATOR!')

e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first = e.get()
    global first_num
    global math
    math = 'add'
    first_num = int(first)
    e.delete(0,END)

def button_sub():
    first = e.get()
    global first_num
    global math
    math = 'sub'
    first_num = int(first)
    e.delete(0, END)

def button_mult():
    first = e.get()
    global first_num
    global math
    math = 'mult'
    first_num = int(first)
    e.delete(0, END)

def button_div():
    first = e.get()
    global first_num
    global math
    math = 'div'
    first_num = int(first)
    e.delete(0, END)

def button_equal():
    second = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, first_num + int(second))
    elif math == 'sub':
        e.insert(0, first_num - int(second))
    elif math == 'mult':
        e.insert(0, first_num * int(second))
    elif math == 'div':
        e.insert(0, first_num / int(second))


#create buttons
button1 = Button(window, text='1', padx=40, pady=40, command=lambda: button_click(1))
button2 = Button(window, text='2', padx=40, pady=40, command=lambda: button_click(2))
button3 = Button(window, text='3', padx=40, pady=40, command=lambda: button_click(3))
button4 = Button(window, text='4', padx=40, pady=40, command=lambda: button_click(4))
button5 = Button(window, text='5', padx=40, pady=40, command=lambda: button_click(5))
button6 = Button(window, text='6', padx=40, pady=40, command=lambda: button_click(6))
button7 = Button(window, text='7', padx=40, pady=40, command=lambda: button_click(7))
button8 = Button(window, text='8', padx=40, pady=40, command=lambda: button_click(8))
button9 = Button(window, text='9', padx=40, pady=40, command=lambda: button_click(9))
button0 = Button(window, text='0', padx=40, pady=40, command=lambda: button_click(0))
button_add = Button(window, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(window, text='=', padx=91, pady=20, command=button_equal)
button_clear = Button(window, text='CLEAR', padx=79, pady=39, command= button_clear)

button_sub = Button(window, text='-', padx=41, pady=20, command=button_sub)
button_mult = Button(window, text='*', padx=40, pady=20, command=button_mult)
button_div = Button(window, text='/', padx=45, pady=20, command=button_div)

#Grid buttons on screen
button1.grid(row=3 , column=0 )
button2.grid(row=3 , column=1 )
button3.grid(row=3 , column=2 )

button4.grid(row=2 , column=0 )
button5.grid(row=2 , column=1 )
button6.grid(row=2 , column=2 )

button7.grid(row=1 , column=0 )
button8.grid(row=1 , column=1 )
button9.grid(row=1 , column=2 )

button0.grid(row=4 , column=0 )

button_add.grid(row=5, column=0)
button_equal.grid(row=5 ,column=1, columnspan=2)
button_clear.grid(row=4 ,column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)

#main loop that runs program
window.mainloop()
