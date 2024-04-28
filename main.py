from tkinter import *
from tkinter.messagebox import *

# some useful variables
font = ('Verdana', 22, 'bold')


# important functions

def all_clear():
    textField.delete(0,END)

def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


def click_btn_function(event):
    print('btn clicked')
    b=event.widget
    text=b['text']
    print(text)

    if text=='=':
        try:
            ex=textField.get()
            answer=eval(ex)
            textField.delete(0,END)
            textField.insert(0,answer)
        except Exception as e:
            print("Error.... ", e)
            showerror("Error",e)
        return

    textField.insert(END,text)

# creating a window
window=Tk()
window.title('My Calculator')
window.geometry('500x650')


# picture label
pic = PhotoImage(file='img/cal6.png')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP,pady=15)

# heading label
heading = Label(window, text='My Calculator', font=font)
heading.pack(side=TOP)

# textfield
textField = Entry(window, font=font, justify= CENTER)
textField.pack(side=TOP, pady=15, fill = X, padx = 15)

# buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
        btn.grid(row=i, column=j, padx=5, pady=5)
        temp+=1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn= Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
zeroBtn.grid(row=3, column=0, padx=5, pady=5)


dotBtn= Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
dotBtn.grid(row=3, column=1, padx=5, pady=5)

equalBtn= Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
equalBtn.grid(row=3, column=2, padx=5, pady=5)

plusBtn= Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
plusBtn.grid(row=0, column=3, padx=5, pady=5)

minusBtn= Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
minusBtn.grid(row=1, column=3, padx=5, pady=5)

multiplyBtn= Button(buttonFrame, text='*', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
multiplyBtn.grid(row=2, column=3, padx=5, pady=5)

divideBtn= Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
divideBtn.grid(row=3, column=3, padx=5, pady=5)

clearBtn= Button(buttonFrame, text='clear', font=font, width=11, relief='ridge', activebackground='orange', activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

allClearBtn= Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='orange', activeforeground='white', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# binding all buttons
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multiplyBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)


# functions for scientific calculator
scFrame = Frame(window)

sqrtBtn= Button(scFrame, text='√', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
sqrtBtn.grid(row=0, column=0, padx=5, pady=5)

powBtn= Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
powBtn.grid(row=0, column=1, padx=5, pady=5)

factBtn= Button(scFrame, text='X!', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
factBtn.grid(row=0, column=2, padx=5, pady=5)

redBtn= Button(scFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
redBtn.grid(row=0, column=3, padx=5, pady=5)

degBtn= Button(scFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
degBtn.grid(row=1, column=0, padx=5, pady=5)


sinBtn= Button(scFrame, text='sinΘ', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
sinBtn.grid(row=1, column=1, padx=5, pady=5)

cosBtn= Button(scFrame, text='cosΘ', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
cosBtn.grid(row=1, column=2, padx=5, pady=5)

tanBtn= Button(scFrame, text='tanΘ', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
tanBtn.grid(row=1, column=3, padx=5, pady=5)


normalcalc = True
def sc_click():
    global normalcalc
    if normalcalc:
        buttonFrame.pack_forget()
        # add sc frame
        scFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP, pady=20)
        window.geometry('500x750')

        print('show sc')
        normalcalc = False
    else:
        scFrame.pack_forget()
        print('show normal')
        normalcalc = True

# creating menu
fontMenu = ('', 15)
menuBar = Menu(window)

mode = Menu(menuBar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label='Scientific Calculator', command=sc_click)

menuBar.add_cascade(label='Mode', menu=mode)

window.config(menu=menuBar)

window.mainloop()