import time
startTime = time.time()
from calculator import Calculator
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("500x500")
root.title("Calculator")
root.minsize(width=200,height=300)

tests = {
    "1-1":0,
    "1+1":2,
    "2*3":6,
    "6/3":2,
    "2^3":8,
    "5\\2":1,
    "25%":0.25,
    "4!":24,
    "p(4,3)":3,
    "c(4,3)":1,
    "Sin(90)":1,
    "log2(4)":2,
    "(2+2)":4,
    "1-1+1+1+2*3+6/3+2^3+5\\2+25%+4!+p(4,3)+c(4,3)+Sin(90)+log2(2+2)":54.25,
}

def addData(val):
    data.set(data.get()+val)
    
def rem():
    data.set(data.get()[:-1])

def remAll():
    data.set("")

def run():
    calc = Calculator()
    print(f"Sent: {data.get()}")
    result = calc.calculate(data.get())
    data.set(result)
    print(f"Got: {result}")


dataFrame = Frame(root,padding=2)
buttonFrame = Frame(root,padding=2)
dataFrame.place(relwidth=1,relheight=.2,relx=0,rely=0.02)
buttonFrame.place(relwidth=1,relheight=.7,relx=0,rely=.22)


data = StringVar()
entry_ = Entry(dataFrame,textvariable=data)

pw = 0.02
ph = 0.02
w = (1-pw)/5 - pw
h = (1-ph)/6 - ph
wp = w + pw
hp = h + ph

#First Row
Button(buttonFrame, text="7", command=lambda: addData("7")).place(anchor='nw',relwidth=w,relheight=h,relx=0*wp+pw,rely=0*hp+ph)
Button(buttonFrame, text="8", command=lambda: addData("8")).place(anchor='nw',relwidth=w,relheight=h,relx=1*wp+pw,rely=0*hp+ph)
Button(buttonFrame, text="9", command=lambda: addData("9")).place(anchor='nw',relwidth=w,relheight=h,relx=2*wp+pw,rely=0*hp+ph)
Button(buttonFrame, text="+", command=lambda: addData("+")).place(anchor='nw',relwidth=w,relheight=h,relx=3*wp+pw,rely=0*hp+ph)
Button(buttonFrame, text="CR", command=lambda: rem()).place(anchor='nw',relwidth=w,relheight=h,relx=4*wp+pw,rely=0*hp+ph)

#Second Row
Button(buttonFrame, text="4", command=lambda: addData("4")).place(anchor='nw',relwidth=w,relheight=h,relx=0*wp+pw,rely=1*hp+ph)
Button(buttonFrame, text="5", command=lambda: addData("5")).place(anchor='nw',relwidth=w,relheight=h,relx=1*wp+pw,rely=1*hp+ph)
Button(buttonFrame, text="6", command=lambda: addData("6")).place(anchor='nw',relwidth=w,relheight=h,relx=2*wp+pw,rely=1*hp+ph)
Button(buttonFrame, text="-", command=lambda: addData("-")).place(anchor='nw',relwidth=w,relheight=h,relx=3*wp+pw,rely=1*hp+ph)
Button(buttonFrame, text="CLR", command=lambda: remAll()).place(anchor='nw',relwidth=w,relheight=h,relx=4*wp+pw,rely=1*hp+ph)

#Third Row
Button(buttonFrame, text="1", command=lambda: addData("1")).place(anchor='nw',relwidth=w,relheight=h,relx=0*wp+pw,rely=2*hp+ph)
Button(buttonFrame, text="2", command=lambda: addData("2")).place(anchor='nw',relwidth=w,relheight=h,relx=1*wp+pw,rely=2*hp+ph)
Button(buttonFrame, text="3", command=lambda: addData("3")).place(anchor='nw',relwidth=w,relheight=h,relx=2*wp+pw,rely=2*hp+ph)
Button(buttonFrame, text="*", command=lambda: addData("*")).place(anchor='nw',relwidth=w,relheight=h,relx=3*wp+pw,rely=2*hp+ph)
Button(buttonFrame, text="/", command=lambda: addData("/")).place(anchor='nw',relwidth=w,relheight=h,relx=4*wp+pw,rely=2*hp+ph)

#Fourth Row
Button(buttonFrame, text=".", command=lambda: addData(".")).place(anchor='nw',relwidth=w,relheight=h,relx=0*wp+pw,rely=3*hp+ph)
Button(buttonFrame, text="0", command=lambda: addData("0")).place(anchor='nw',relwidth=w,relheight=h,relx=1*wp+pw,rely=3*hp+ph)
Button(buttonFrame, text=",", command=lambda: addData(",")).place(anchor='nw',relwidth=w,relheight=h,relx=2*wp+pw,rely=3*hp+ph)
Button(buttonFrame, text="P(n,r)", command=lambda: addData("P(")).place(anchor='nw',relwidth=w,relheight=h,relx=3*wp+pw,rely=3*hp+ph)
Button(buttonFrame, text="C(n,r)", command=lambda: addData("C(")).place(anchor='nw',relwidth=w,relheight=h,relx=4*wp+pw,rely=3*hp+ph)

#Fiftn Row
Button(buttonFrame, text="\\", command=lambda: addData("\\")).place(anchor='nw',relwidth=w,relheight=h,relx=0*wp+pw,rely=4*hp+ph)
Button(buttonFrame, text="^", command=lambda: addData("^")).place(anchor='nw',relwidth=w,relheight=h,relx=1*wp+pw,rely=4*hp+ph)
Button(buttonFrame, text="%", command=lambda: addData("%")).place(anchor='nw',relwidth=w,relheight=h,relx=2*wp+pw,rely=4*hp+ph)
Button(buttonFrame, text="Sin", command=lambda: addData("Sin(")).place(anchor='nw',relwidth=w,relheight=h,relx=3*wp+pw,rely=4*hp+ph)
Button(buttonFrame, text="Cos", command=lambda: addData("Cos(")).place(anchor='nw',relwidth=w,relheight=h,relx=4*wp+pw,rely=4*hp+ph)

#Sixth Row
Button(buttonFrame, text="!", command=lambda: addData("!")).place(anchor='nw',relwidth=w,relheight=h,relx=0*wp+pw,rely=5*hp+ph)
Button(buttonFrame, text="(", command=lambda: addData("(")).place(anchor='nw',relwidth=w,relheight=h,relx=1*wp+pw,rely=5*hp+ph)
Button(buttonFrame, text=")", command=lambda: addData(")")).place(anchor='nw',relwidth=w,relheight=h,relx=2*wp+pw,rely=5*hp+ph)
Button(buttonFrame, text="Tan", command=lambda: addData("Tan(")).place(anchor='nw',relwidth=w,relheight=h,relx=3*wp+pw,rely=5*hp+ph)
Button(buttonFrame, text="=", command=lambda: run()).place(anchor='nw',relwidth=w,relheight=h,relx=4*wp+pw,rely=5*hp+ph)


entry_.place(anchor='n',relx=0.55,rely=0.01,relwidth=0.8,relheight=0.8)
entry_.bind('<KeyPress-Return>',lambda event: run())

if __name__ == "__main__":
    print(f"Time Taken: {int((time.time()-startTime)*1000)}ms")
    root.mainloop()