# from tkinter import messagebox
# from tkinter import*
# root =Tk()
# root.geometry("400x400")
# def display():
#     messagebox.showinfo("information","login success")
#     messagebox.showwarning("warning","it only consists of alphabets and spaces")
#     messagebox.showerror("error","login error")
#     messagebox.askokcancel("ask question","are you sure")
#     messagebox.askyesno("ask question","are you sure")
#     messagebox.askretrycancel("ask question","are you sure")
#     x=messagebox.askquestion("ask question","are you sure")
#     print(x)

# b1 = Button(root,text="click",command=display)
# b1.grid(row=1,column=1)
# root.mainloop()


# from tkinter import messagebox
# from tkinter import*
# root =Tk()
# root.geometry("400x400")
# def display():
#     x=messagebox.askyesno("ask question","are you sure")
#     print(x)
#     if x==True:
#         messagebox.showinfo("information","success")
#     else:
#         messagebox.showinfo("information","cancel")

# b1 = Button(root,text="click",command=display)
# b1.grid(row=1,column=1)

# root.mainloop()


# from tkinter import messagebox
# from tkinter import*
# root =Tk()
# root.geometry("400x400")

# count = 0
# def display():
#     global count
#     count+=1
#     l1 = Label(root,text="clicked "+str(count)+" times")
#     l1.grid(row=2,column=4)

# b1 = Button(root,text="click",command=display)
# b1.grid(row=1,column=1)
# l1 = Label(root,text="clicked "+str(count)+" times")
# l1.grid(row=2,column=4)

# root.mainloop()


# radibutton
from tkinter import messagebox
from tkinter import*
root =Tk()
root.geometry("400x400")

# strvar kodthal ellam select aavm
# intvar kodthal onnm selct aavilla
# int var kodthitt 0 value aaitt evidelm indel ath select aai varm
# s = StringVar()
s = IntVar()
r1 = Radiobutton(root,text="female",variable=s,value=1)
r1.grid(row=1,column=1)
r2 = Radiobutton(root,text="male",variable=s,value=2)
r2.grid(row=2,column=1)
r3 = Radiobutton(root,text="others",variable=s,value=3)
r3.grid(row=3,column=1)

r1 = Radiobutton(root,text="python",variable=s,value=1)
r1.grid(row=1,column=1)
r2 = Radiobutton(root,text="java",variable=s,value=2)
r2.grid(row=2,column=1)
r3 = Radiobutton(root,text="php",variable=s,value=3)
r3.grid(row=3,column=1)
root.mainloop()


# checkbutton
from tkinter import messagebox
from tkinter import*
root =Tk()
root.geometry("400x400")

c1 = Checkbutton(root,text="english").grid(row=1,column=1)
c2 = Checkbutton(root,text="hindi").grid(row=2,column=1)
c3 = Checkbutton(root,text="malayalam").grid(row=3,column=1)

root.mainloop()




