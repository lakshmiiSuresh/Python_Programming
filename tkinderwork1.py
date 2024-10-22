# from tkinter import*
# x=Tk()
# x.title("welcome to tkinder window")
# x.geometry("400x400") 

# l = Label(x,text="name",bd=5)
# l.grid(row=1,column=1)
# e1 = Entry(x,show="")
# e1.grid(row=1,column=2)

# l2 = Label(x,text="Address",bd=5)
# l2.grid(row=2,column=1)
# e2 = Entry(x,show="")
# e2.grid(row=2,column=2)

# l3 = Label(x,text="Ph number",bd=5)
# l3.grid(row=3,column=1)
# e3 = Entry(x,show="")
# e3.grid(row=3,column=2)

# # global l4,l5,l6,l7,l8,l9
# def submit():
#     global l4,l5,l6,l7,l8,l9,l10,l11
#     e1.get()
#     e2.get()
#     e3.get()
#     l8 = Label(x,text="Details:")
#     l8.grid(row=7,column=2)

#     l9 = Label(x,text="Name:")
#     l9.grid(row=8,column=2)
#     l5= Label(x,text=e1.get())
#     l5.grid(row=8,column=3)

#     l10= Label(x,text="Address:")
#     l10.grid(row=9,column=2)
#     l6 = Label(x,text=e2.get())
#     l6.grid(row=9,column=3)


#     l11 = Label(x,text="Ph number:")
#     l11.grid(row=10,column=2)
#     l7= Label(x,text=e3.get())
#     l7.grid(row=10,column=3)

   
# b1 = Button(x,text="submit",command=submit)
# b1.grid(row=6,column=2)

# def delete():
#     l8.destroy()
#     l9.destroy()
#     l5.destroy()
#     l10.destroy()
#     l6.destroy()
#     l11.destroy()
#     l7.destroy()
    

# b2 = Button(x,text="delete",background="black",foreground="white",command=delete)
# b2.grid(row=6,column=3)

# x.mainloop()



# ------------------------------------
# from tkinter import*
# x = Tk()
# x.geometry("400x400") 

# a=StringVar()
# l1 = Label(x,text="FIRST NUMBER")
# l1.pack()
# e1 = Entry(x,show="")
# e1.pack()

# l2 = Label(x,text="SECOND NUMBER")
# l2.pack()
# e2 = Entry(x,show="")
# e2.pack()

# l3 = Label(x,text="RESULT")
# l3.pack()
# e3 = Entry(x,show="",textvariable=a)
# e3.pack()

# def findsum():
#     s = int(e1.get())+int(e2.get())
#     a.set(s)

# b1 = Button(x,text="FIND SUM",command=findsum)
# b1.pack()

# x.mainloop()


