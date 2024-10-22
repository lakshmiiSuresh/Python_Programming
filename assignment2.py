
# create a class having 2 methods . one getting multiple phonenumbers and other for multiple emails
class Details:
    def add_phone(self):
       self.l1=[]
       self.l1.append(int(input("Enter your number: ")))
       while True:
            ch = input("Do you want to add? Y or N ").upper()
            if ch=='Y':
                num = int(input("Enter another number", ))
                self.l1.append(num)
            elif ch=='N':
                break
       return self.l1

    def add_email(self):
        self.l2=[]
        self.l2.append(input("Enter your Email: "))
        while True:
            ch = input("Do you want to add? Y or N ").upper()
            if ch=='Y':
                email = input("Enter another email", )
                self.l2.append(email)
            elif ch=='N':
                break   
        return self.l2


# create another class - initialize values name address phlist email list
class Details_info:
      dict1={}
      def __init__(self,name,address,ph_list,em_list):
        self.name=name
        self.address=address
        self.ph_list=ph_list
        self.em_list=em_list

      def addContact(self):
        self.dict1[self.name]= {"name":self.name,"address":self.address,"phone number":self.ph_list,"Email":self.em_list}
        print(self.dict1)
        print("Contact added successfully")

    #   def view(self):
    #     # print("Name:",self.name)
    #     # print("Address:",self.address)
    #     # print("Phone number:",self.ph_list)
    #     # print("Email :",self.em_list)
    #     print(self.dict1)

      def updateContact(self,u_name):
        if u_name in self.dict1.keys():
            while True:
                detail = int(input("1.name \n2.address\n3.phone number\n4.email\n5.Add other detail\n6.Exit\nSelect any: "))
                if detail==1:
                    self.new_name = input('Enter new name: ')
                    self.dict1[u_name].update({"name":self.new_name})
                    self.x = self.dict1.pop(u_name)
                    dict1[self.new_name]=self.x
                    print(self.dict1)
                    break
                
                elif detail==2:
                    self.new_address = input("Enter new address: ")
                    self.dict1[u_name].update({"address":self.new_address})
                    print(self.dict1)

                elif detail==3:
                    n = int(input("\n1.Add \n2.Update:\n"))
                    if n==1:
                        self.dict1[u_name]["phone number"].append(int(input("Enter new number: ")))
                        print(self.dict1)

                    elif n==2:
                        pos = int(input("Enter the position of number: "))
                        new_number=int(input("Enter the new number: "))
                        self.dict1[u_name]["phone number"][pos-1]=new_number
                        print(self.dict1)

                elif detail==4:
                    e = int(input("\n1.Add \n2.Update "))
                    if e==1:
                        self.dict1[u_name]["Email"].append(input("Enter new email: "))
                        print(self.dict1)

                    elif e==2:
                        pos = int(input("Enter the position of email: "))
                        new_email=input("Enter the new email: ")
                        self.dict1[u_name]["Email"][pos-1]=new_email
                        print(self.dict1)
                
                elif detail==5:
                    new_detail = input("Enter new detail: ")
                    new_value = input("Enter value")
                    self.dict1[u_name][new_detail]=new_value
                    
                elif detail==6:
                    break
        else:
            print("Name not found")


      def deleteContact(self,d_name):
        if d_name in self.dict1.keys():
            while True:
                ch = int(input("\n1.Name\n2.Address\n3.Phone number\n4.Email\n5.exit\nEnter which detail to be deleted: "))
                if ch==1:
                    self.dict1[d_name].pop(d_name)
                    print(dict1)
                    break

                elif ch==2:
                    self.dict1[d_name].pop("address")
                    print(dict1)

                elif ch==3:
                    ch1 = input("Delete all numbers? y or n ")
                    if ch1 == 'y':
                        self.dict1[d_name].pop("phone number")
                        print(self.dict1)
                    elif ch1 == 'n':
                        num = int(input("Which phone number: "))
                        if num in self.dict1[d_name]["phone number"]:
                            self.dict1[d_name]["phone number"].remove(num)
                        print(self.dict1)
                        # ph_pos = int(input("Enter the position of number which you want to delete: "))
                        # del self.dict1[d_name]["phonenumber"][ph_pos-1]
                        # print(self.dict1)
                elif ch==4:
                    ch1 = input("Delete all emails? y or n ")
                    if ch1 == 'y':
                        self.dict1[d_name].pop("Email")
                        print(self.dict1)
                    elif ch1 == 'n':
                        em = input("Which email ")
                        if em in self.dict1[d_name]["Email"]:
                            self.dict1[d_name]["Email"].remove(em)
                        print(self.dict1)
                       
                elif ch==5:
                    break
        else:
            print("Name not found")

      def veiwContact(self,v_name):
        if v_name in self.dict1.keys():
            print(self.dict1[v_name])
  
      
      def viewAll(self):
        print(self.dict1)
          
 
while True:
    dict1={}
    choice = int(input("Select your choice: \n1.Add \n2.Update \n3.Delete \n4.View a contact \n5.View all contact \n6.Exit \nEnter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        d = Details()
        ph_list = d.add_phone()
        em_list = d.add_email()
        d1 = Details_info(name,address,ph_list,em_list)
        d1.addContact()

    elif choice==2:
        u_name = input("Enter whose detail do you want to update: ")
        d1.updateContact(u_name)

    elif choice==3:
        d_name=input("Enter whose detail you want to delete: ")
        d1.deleteContact(d_name)

    elif choice==4:
        v_name=input("Enter name to view details: ")
        d1.veiwContact(v_name)

    elif choice==5:
        d1.viewAll()

    elif choice==6:
        break



