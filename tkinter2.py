from tkinter import *
from tkinter.ttk import Combobox,Progressbar
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from PIL import Image

x = Tk()
# combobox
# cc = Combobox(x)
# cc["values"]=["p","l","k","m"]
# # cc.current(2)
# cc.grid(row=11,column=2)

# spinbox
# when clicked in u arrow it goes form 1 to 10
# s = Spinbox(x,from_=1,to=10).grid(row=12,column=2)

# scrolledtext
# s1 = ScrolledText(x,widt=5,height=5).grid(row=13,column=2)

# progressbar
# p=Progressbar(x,length=800)
# p['value']=50
# p.grid(row=15,column=4)

# # filedialog
# def fileclick():
#     u = filedialog.askopenfilename()
# bb = Button(x,text="click",bg="red",fg="yellow",bd=5,command=fileclick())
# bb.grid(row=22,column=5)

#=======================================
# frame
# f1 = Frame(x,highlightbackground="blue",highlightthickness=5)
# f1.grid(row=0,column=0,ipadx=100,ipady=100,padx=10,pady=10) #ipadx,ipady ullil ullath
# f2 = Frame(x,highlightbackground="red",highlightthickness=5)
# f2.grid(row=0,column=3,ipadx=200,ipady=200,padx=40,pady=40)#padx,pady purath ulla padding

# l = Label(f1,text="name") # to write label inside frame f1 - instead of x write f1
# l.grid(row=1,column=1)


#only support .png images in tkinter
# img = PhotoImage(file="./sky.png")
# l = Label(f1,image=img)
# l.grid(row=1,column=1)

# to convert to png
# from PIL import Image
# img = Image.open("Image.jpeg")
# img.save("imageee.png","PNG")

# ======================================
# canvas
# image_path="./sky.png"
# img = PhotoImage(file=image_path)
# canvas = Canvas(x,width=img.width(),height=img.height())# to make it full screen width and height methods sare used
# canvas.pack()
# canvas.create_image(0,0,anchor=NW,image=img)
# canvas.create_text(100,50,text="SURVEY FORM",font=("Helvectica",20),fill="white")

# =====================================
# # pack -side(top,bottom,left,right)
# l = Label(x,text="name",bg="red")
# l.pack(side=TOP,)
# l = Label(x,text="name",bg="green")
# l.pack(side=BOTTOM)
# l = Label(x,text="name")
# l.pack(side=LEFT)
# l = Label(x,text="name")
# l.pack(side=RIGHT)

# # pack -side il expand um fill um
# l = Label(x,text="name",bg="red")
# l.pack(side=TOP,expand=True,fill=BOTH)
# l = Label(x,text="name",bg="green")
# l.pack(side=BOTTOM,expand=True,fill=BOTH)

# pack - fill and expand
# l = Label(x,text="name",bg="red")
# l.pack(fill=X,expand=True)
# l = Label(x,text="name",bg="green")
# l.pack(fill=Y,expand=True)
# l = Label(x,text="name",bg="blue")
# l.pack(fill=BOTH,expand=True)
# l = Label(x,text="name",bg="yellow")
# l.pack(fill=BOTH,expand=True)

# pack- padx,pady
# l = Label(x,text="name",bg="red")
# l.pack(padx=20,pady=20)
# l = Label(x,text="name",bg="green")
# l.pack(ipadx=40,ipady=40)
# l = Label(x,text="name",bg="blue")
# l.pack(ipadx=20,ipady=20)
# l = Label(x,text="name",bg="yellow")
# l.pack(padx=40,pady=40)


# =======================================================
# menu
menu = Menu(x)
new = Menu(menu,tearoff=False) #tearoff to remove dotted line,new menu is for file if new instance is given in file label
new1 = Menu(menu,tearoff=False)
newmenu = Menu(new,tearoff=False)
menu.add_cascade(label="file",menu=new)
menu.add_cascade(label="edit",menu=new1)
menu.add_cascade(label="View")
menu.add_cascade(label="exit",command=x.quit)

new.add_command(label="new file")#add command to add items in drop down
newmenu.add_command(label="hai")
new.add_command(label="new folder")
new.add_separator()
new.add_command(label="open new file")
new.add_command(label="open new folder")

#drop down for edit
new1.add_command(label="undo")
new1.add_command(label="redo")
new1.add_separator()
new1.add_command(label="cut")
new1.add_command(label="copy")
new1.add_command(label="paste")

x.configure(menu=menu)#display menu

x.mainloop()

# generator - yeild
# complte survey form
# calcul
