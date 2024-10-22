# from tkinter import*
# from tkinter import filedialog
# from tkinter.ttk import Combobox
# x = Tk()
# x.geometry("400x400")

# l1 = Label(x,text="let us know how we can help")
# l1.grid(row=2,column=10)

# l2 = Label(x,text="Name")
# l2.grid(row=3,column=10)
# e1 = Entry(x,show="")
# e1.grid(row=3,column=11)


# l3 = Label(x,text="Email")
# l3.grid(row=4,column=10)
# e2 = Entry(x,show="")
# e2.grid(row=4,column=11)

# l4 = Label(x,text="Age")
# l4.grid(row=5,column=10)
# e3 = Entry(x,show="")
# e3.grid(row=5,column=11)

# l5 = Label(x,text="Which option best decribes your current role")
# l5.grid(row=6,column=10)
# c = Combobox(x)
# c["values"]=["student","teacher","doctor"]
# c.grid(row=6,column=11)

# l5 = Label(x,text="How likely is that you would reccomend this program to a friend")
# l5.grid(row=6,column=10)
# x.mainloop()



#====================================
#inside frame
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import Image

x = Tk()
x.geometry("400x300")

img = Image.open("skyy.jpg")
img.save("skyyyy.png","PNG")
imga = PhotoImage(file="skyyyy.png")
canvas = Canvas(x)# to make it full screen width and height methods sare used
canvas.grid(row=0,column=0)
canvas.create_image(0,0,anchor=NW,image=imga)

#frame
f = Frame(x,highlightbackground="white",highlightthickness=5)
f.grid(row=0,column=0,ipadx=100,ipady=100,padx=10,pady=10)


l1 = Label(f,text="let us know how we can help")
l1.grid(row=5,column=100)

l2 = Label(f,text="Name")
l2.grid(row=6,column=100)
e1 = Entry(f,show="")
e1.grid(row=6,column=110)


l3 = Label(f,text="Email")
l3.grid(row=7,column=100)
e2 = Entry(f,show="")
e2.grid(row=7,column=110)

l4 = Label(f,text="Age")
l4.grid(row=8,column=50)
e3 = Entry(f,show="")
e3.grid(row=8,column=60)

# l5 = Label(f,text="Which option best decribes your current role")
# l5.place(x=60,y=30)
# c = Combobox(f)
# c["values"]=["student","teacher","doctor"]
# c.place(x=60,y=30)

# l5 = Label(f,text="How likely is that you would reccomend this program to a friend")
# l5.place(x=70,y=30)
# s = IntVar()
# r1 = Radiobutton(f,text="Definitely",variable=s,value=1)
# r1.place(x=80,y=30)
# r2 = Radiobutton(f,text="Maybe",variable=s,value=2)
# r2.place(x=90,y=30)
# r3 = Radiobutton(f,text="Not sure",variable=s,value=3)
# r3.place(x=100,y=30)

# l5 = Label(f,text="What do you like most here")
# l5.place(x=101,y=30)
# cc = Combobox(f)
# cc["values"]=["select an option","teaching","cls"]
# cc.current("0")
# cc.place(x=101,y=30)

# l5 = Label(f,text="Things that should be improved in the future?")
# l5.place(x=20,y=30)
# s = IntVar()
# r11 = Radiobutton(f,text="Front end projects",variable=s,value=1)
# r11.place(x=20,y=30)
# r22 = Radiobutton(f,text="backend projects",variable=s,value=2)
# r22.place(x=20,y=30)
# r33 = Radiobutton(f,text="data visualization",variable=s,value=3)
# r33.place(x=20,y=30)


# l5 = Label(f,text="Any comments or suggestions")
# l5.place(x=20,y=30)
# s = Spinbox(x,from_=1,to=10).place(x=20,y=30)


x.mainloop()
