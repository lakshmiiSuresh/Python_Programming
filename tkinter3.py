from tkinter import*
from tkinter.scrolledtext import ScrolledText

root = Tk()
# root.title("Tkinter background image example")
# img = PhotoImage(file=r"C:\Users\SURESH\OneDrive\Desktop\sky.png.png") #to change small icon in the window
# root.iconphoto(True,img)

# s = IntVar()
# r1 = Radiobutton(root,text="female",variable=s,value=0)
# r1.grid(row=1,column=1)
# r2 = Radiobutton(root,text="male",variable=s,value=1)
# r2.grid(row=2,column=1)
# r3 = Radiobutton(root,text="others",variable=s,value=2)
# r3.grid(row=3,column=1)

#insert into scrolled text when click button is clicked
# delete text from scrolled text
def show():
    # s.insert(1.0,"hai\n") #first row zeroth column
    # s.insert(4.0,"hai\n")
    # s.delete('1.0',END)
    s.delete('1.2','1.end')

s = ScrolledText(root,width=10,height=10)
s.grid(row=3,column=4)

b = Button(root,text="click",command=show)
b.grid(row=10,column=0)

root.mainloop()