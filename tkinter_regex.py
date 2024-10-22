# form using tkinter and regular expression
from tkinter import*
from tkinter import messagebox
import re
root = Tk()

root.geometry("500x500")

l1 = Label(root,text="Name")
l1.place(x=100,y=100)
e1 = Entry(root,show="")
e1.place(x=250,y=100)


l2 = Label(root,text="Phone number")
l2.place(x=100,y=150)
e2 = Entry(root,show="")
e2.place(x=250,y=150)

l3 = Label(root,text="Email")
l3.place(x=100,y=200)
e3 = Entry(root,show="")
e3.place(x=250,y=200)

l4 = Label(root,text="Password")
l4.place(x=100,y=250)
e4 = Entry(root,show="")
e4.place(x=250,y=250)


l5 = Label(root,text="Confirm Password")
l5.place(x=100,y=300)
e5 = Entry(root,show="")
e5.place(x=250,y=300)
def submit():
    count=0
    if e1.get()=="" and e2.get()=="" and e3.get()=="" and e4.get()=="":
        messagebox.showerror("Error", "Fields are empty")
        # return
    
    name1 = e1.get()
    print(name1)
    r1 = re.findall(r"[^a-zA-Z\s]",name1)
    r2 = re.findall(r"\A[a-zA-Z]",name1)
    if r1!=[] and r2:
         count+=1     
    else:
        messagebox.showerror("Error", "Invalid name")
        # return
    

    phonenumber = e2.get()
    p = re.findall(r"\b[6789]\d{9}\b",phonenumber)
    if not p:
        messagebox.showerror("Error", "Invalid phone number.")
        # return
    else:
        count+=1

    email =e3.get()
    e = re.findall(r"\A[a-z0-9]+@[a-z0-9]+\.[a-z]+",email)
    if not e:
        messagebox.showerror("Error", "Incorrect email format(format:abc@gmail.com)")
        # return
    else:
        count+=1
    
    passw = e4.get()
    pa = re.findall("[A-Za-z\d@$!%*?&#]+",passw)
    if not pa:
        messagebox.showerror("Error", "Password cannot be empty")
        # return
    else:
        count+=1

    cpassw = e5.get()
    if passw != cpassw:
        messagebox.showerror("error","Re Enter password correctly")
        # return
    else:
        count+=1
    
    print(count)
    if count==5:
        l.configure(text="Form submitted successfully")
    else:
        l.configure(text="Form submitted unsuccessfully")

l = Label(root,text="")
l.place(x=200,y=370)

b = Button(root,text="Submit",command=submit)
b.place(x=250,y=400)

root.mainloop()

