
from tkinter import *
from tkinter import ttk
from tkinter import font
#import time
import datetime
def quit(*args):
    root.destroy()
def clock_time():
    time=datetime.datetime.now()
    time=(time.strftime("%d-%B-%Y & %I:%M:%S %p"))
    #time=(time.strftime("%H:%M:%S"))
    txt.set(time)
    root.after(1000,clock_time)
root=Tk()
root.attributes("-fullscreen",True)
bg = PhotoImage(file = "img.png")
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 10, y = 100)
#root.configure(background='yellow')
root.bind("x",quit)
root.after(1000,clock_time)
fnt=font.Font(family='Times',size=80,weight='normal')
txt=StringVar()
lbl=ttk.Label(root,textvariable=txt,font=fnt,foreground="white",background="black")
lbl.place(relx=0.45,rely=0.23,anchor=CENTER)
root.mainloop()
