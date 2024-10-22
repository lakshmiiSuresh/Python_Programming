from tkinter import*
x=Tk() #tk nn parayunna clsinu oru instance 
x.title("welcome to tkinder window")
x.geometry("400x400") #for size of window

# x.resizable("width","height")
# x.resizable(True,False)
# x.resizable(False,True)
# x.resizable(False,False)
# x.resizable(True,True)

# x.attributes("-alpha",0.5) #range 0-1, for opacity
# x.attributes("-alpha",0)#window not visible for value 0

# x.attributes("-topmost",1)#vere evidem click cheythal window pokillah
# x.attributes("-topmost",0)#vere evidelm click aakiyal window pokm

# l=Label(x,text="name",bg="red",fg="yellow",width=10,height=3,anchor="nw",font="arial 10 bold")
# l.grid(row=1,column=1)

# l1=Label(x,text="course",background="blue",foreground="white")
# l1.grid(row=2,column=1)

# l1=Label(x,text="course")
# l1.grid(row=10,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="nw",font="arial 10 italic",cursor="plus")
# l.grid(row=11,column=1)

# l=Label(x,text="name",bg="green",fg="white",width=10,height=3,anchor="ne",font="arial 10 underline",cursor="clock")
# l.grid(row=12,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="se",font="arial 10 overstrike",cursor="circle")
# l.grid(row=13,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="s",font="arial 10 underline",cursor="circle")
# l.grid(row=13,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="n",font="arial 10 italic",cursor="circle")
# l.grid(row=14,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="se",font="arial 10 italic",cursor="circle")
# l.grid(row=15,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="s",font="arial 10 italic",cursor="circle")
# l.grid(row=16,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="s",font="arial 10 italic",cursor="circle")
# l.grid(row=17,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="s",font="arial 10 italic",cursor="circle")
# l.grid(row=18,column=1)

# l=Label(x,text="name",bg="red",fg="white",width=10,height=3,anchor="s",font="arial 10 italic",cursor="circle")
# l.grid(row=19,column=1)

# l=Label(x,text="name",bg="red",font="arial 10 italic",cursor="circle")
# l.grid(row=1,column=1)
# e1 = Entry(x,show="")
# e1.grid(row=1,column=2)
# e1 = Entry(x,show="*",justify="right",bd=5,bg="red",fg="white")
# e1.grid(row=1,column=2)
# e1 = Entry(x,show="*",justify="center")
# e1.grid(row=2,column=2)
# e1 = Entry(x,show="*",justify="left")
# e1.grid(row=3,column=2)
# x.configure(bg="black")
# print("start")

# # button
# b1 = Button(x,text="click button")
# b1.grid(row=1,column=0)

# b2 = Button(x,text="click button",font="arial 10 bold underline")
# b2.grid(row=2,column=0)

# b3 = Button(x,text="click button",bg="red",fg="yellow")
# b3.grid(row=3,column=0)

# b4 = Button(x,text="click button",width=10)
# b4.grid(row=17,column=0)

# b4 = Button(x,text="click button",height=5)
# b4.grid(row=18,column=0)

# b5 = Button(x,text="click button",activebackground='green')
# b5.grid(row=5,column=0)

# b6 = Button(x,text="click button",activeforeground='purple')
# b6.grid(row=6,column=0)

# b7 = Button(x,text="click button",bd=10)
# b7.grid(row=7,column=0)

# b8 = Button(x,text="click button",state=DISABLED)
# b8.grid(row=8,column=0)

# b9 = Button(x,text="click button",padx=40)
# b9.grid(row=9,column=0)

# b10 = Button(x,text="click button",pady=40)
# b10.grid(row=10,column=0)

# b11 = Button(x,text="click button")
# b11.grid(row=11,column=0)

# b12 = Button(x,text="SUNKEN",relief=SUNKEN,bd=10)
# b12.grid(row=12,column=0)

# b13 = Button(x,text="RIDGE",relief=RIDGE,bd=10)
# b13.grid(row=13,column=0)

# b14 = Button(x,text="GROOVE",relief=GROOVE,bd=10)
# b14.grid(row=14,column=0)

# b15 = Button(x,text="RAISED",relief=RAISED,bd=10)
# b15.grid(row=15,column=0)

# b16 = Button(x,text="FLAT",relief=FLAT,bd=10)
# b16.grid(row=16,column=0)

# l=Label(x,text="name",bg="red",fg="yellow",width=10,height=3,anchor="nw",font="arial 10 bold")
# l.grid(row=1,column=1)
# a=StringVar()
# e1 = Entry(x,show="",textvariable=a)
# e1.grid(row=1,column=2)
# def click():
#     # print("hello")
#     l.configure(text="changed text")
#     print(e1.get())
#     l.destroy()
#     a.set("hello")
# b17 = Button(x,text="click button",bd=10,command=click)
# b17.grid(row=11,column=0)


# # print("start")
# x.mainloop()#mainloop inte akth ulle mathre window il varuvollu
# # print("stop")

# pack()- responsive  to window
from tkinter import*
window =Tk()
window.title("tkinder project")
window.geometry("400x400")

l1=Label(window,text="name")
l1.pack()
l2=Label(window,text="name")
l2.pack()
l3=Label(window,text="name")
l3.pack()
l4=Label(window,text="name")
l4.pack()
l5=Label(window,text="name")
l5.pack()

window.mainloop()
