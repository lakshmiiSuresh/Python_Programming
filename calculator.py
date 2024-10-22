from tkinter import*
x = Tk()
x.geometry("280x380")

b=StringVar()
e1 = Entry(x,show="",width=45,bd=2,textvariable=b)
e1.grid(row=1,column=1,columnspan=4)
s = ""
flag=False
def click(a):
    global s
    global flag
    if flag==True and s.isdigit():
        s=""
        s+=a
        b.set(s) 
        flag=False
    elif flag==False:
        s+=a
        b.set(s)
        flag=False
    else:
        s+=a
        b.set(s)       

def op():
    global s
    global flag
    s = str(eval(s))
    b.set(s)
    flag = True

def delete():
    global s
    s=""
    b.set(s)
   
def backspace():
    global s
    b.set(s[:-1])

b1 = Button(x,text="clear",background="lightblue",height=4,width=8,command=delete)
b1.grid(row=2,column=1)
b2 = Button(x,text="<",background="lightblue",height=4,width=8,command=backspace)
b2.grid(row=2,column=2)
b3 = Button(x,text="%",background="lightblue",height=4,width=8,command=lambda :click("%"))
b3.grid(row=2,column=3)
b4 = Button(x,text="/",background="lightblue",height=4,width=8,command=lambda :click("/"))
b4.grid(row=2,column=4)

b5 = Button(x,text="7",background="lightblue",height=4,width=8,command=lambda :click("7"))
b5.grid(row=3,column=1)
b6 = Button(x,text="8",background="lightblue",height=4,width=8,command=lambda :click("8"))
b6.grid(row=3,column=2)
b7 = Button(x,text="9",background="lightblue",height=4,width=8,command=lambda :click("9"))
b7.grid(row=3,column=3)
b8 = Button(x,text="*",background="lightblue",height=4,width=8,command=lambda :click("*"))
b8.grid(row=3,column=4)


b9 = Button(x,text="4",background="lightblue",height=4,width=8,command=lambda :click("4"))
b9.grid(row=4,column=1)
b10 = Button(x,text="5",background="lightblue",height=4,width=8,command=lambda :click("5"))
b10.grid(row=4,column=2)
b11= Button(x,text="6",background="lightblue",height=4,width=8,command=lambda :click("6"))
b11.grid(row=4,column=3)
b12= Button(x,text="-",background="lightblue",height=4,width=8,command=lambda :click("-"))
b12.grid(row=4,column=4)


b13 = Button(x,text="1",background="lightblue",height=4,width=8,command=lambda :click("1"))
b13.grid(row=5,column=1)
b14 = Button(x,text="2",background="lightblue",height=4,width=8,command=lambda :click("2"))
b14.grid(row=5,column=2)
b15= Button(x,text="3",background="lightblue",height=4,width=8,command=lambda :click("3"))
b15.grid(row=5,column=3)
b16= Button(x,text="+",background="lightblue",height=4,width=8,command=lambda :click("+"))
b16.grid(row=5,column=4)

b17 = Button(x,text="+/-",background="lightblue",height=4,width=8,command=lambda :click("+/-"))
b17.grid(row=6,column=1)
b18 = Button(x,text="0",background="lightblue",height=4,width=8,command=lambda :click("0"))
b18.grid(row=6,column=2)
b19= Button(x,text=".",background="lightblue",height=4,width=8,command=lambda :click("."))
b19.grid(row=6,column=3)
b20= Button(x,text="=",background="lightblue",height=4,width=8,command=lambda :op())
b20.grid(row=6,column=4)

x.mainloop()