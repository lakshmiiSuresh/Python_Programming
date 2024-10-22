main_dict = {}
while True:
    n = int(input("\nSelect your choice: \n1.Add \n2.View \n3.Add/Update \n4.Delete \n5.Exit \nEnter your choice: "))
    if n == 1:
        print("\nAdd your details:")
        dict1 = {}
        name = input("Enter your name: ")
        dict1["name"] = name

        address = input("Enter your address: ")
      
        phonenum = int(input("How many numbers do you want to enter: "))
        list1 = []
        for i in range(1,phonenum+1):
            num = int(input("Enter number "+ str(i)+ ": "))
            dict1["phonenumber"] = num
            list1.append(dict1["phonenumber"])
        dict1["phonenumber"] = list1
       

        email = int(input("How many emails do you wantt to enter: "))
        list2=[]
        for i in range(1,email+1):
            em = input(("Enter email "+str(i)+": "))
            dict1["email"]= em
            list2.append(dict1["email"])
        dict1["email"] = list2

        main_dict[name]=dict1
        print(main_dict)

        f = open("phonebook.txt","a")
        f.write(str(main_dict))
        f.close()

    elif n==2:
        print("\nYour phonebook:")
        print(main_dict)

    elif n==3:
        while True:
            choice1 = int(input("\n1.Add \n2.Update \n3.exit\nSelect your choice: "))
            if choice1==1:
                print("Add your details:")
                dict1 = {}
                name = input("Enter your name: ")
                dict1["name"] = name

                dict1["address"] = input("Enter your address: ")

                phonenum = int(input("How many numbers do you want to enter: "))
                list1 = []
                for i in range(1,phonenum+1):
                    num = int(input("Enter number "+ str(i)+ ": "))
                    dict1["phonenumber"] = num
                    list1.append(dict1["phonenumber"])
                dict1["phonenumber"] = list1

                email = int(input("How many emails do you wantt to enter: "))
                list2=[]
                for i in range(1,email+1):
                    em = input(("Enter email "+str(i)+": "))
                    dict1["email"]= em
                    list2.append(dict1["email"])
                dict1["email"] = list2

                main_dict[name]=dict1
                print("New person added to phonebook")
                print(main_dict)

            elif choice1==2:
                name = input("Enter whose detail to be updated: ")
                if name in main_dict.keys():
                    detail = int(input("\n1.name \n2.address\n3.phone number\n4.email\nChoose which detail of "+ name +" to be updated: "))

                    if detail==1:
                        new_name = input("Enter the new name to update: ") 
                        main_dict[name].update({"name":new_name})
                        x = main_dict.pop(name)
                        main_dict[new_name]=x
                        print(main_dict)

                    elif detail==2:
                        address = input("Enter the new address")
                        main_dict[name].update({"address":address})
                        print(main_dict)

                    elif detail==3:
                        pos = int(input("which is the position of the number "))
                        new_num = int(input("Enter new number: "))
                        x = main_dict[name]["phonenumber"]
                        x[pos-1]=new_num
                        print(main_dict)

                     
                    elif detail==4:
                        email_pos = int(input("Which is the position of the email you want to update: "))
                        new_email = input("Enter new email: ")
                        y = main_dict[name]["email"]
                        y[email_pos-1] = new_email
                        print(main_dict)
                else:
                    print("Name not found")
                

            elif choice1==3:
                break
            
            else:
                print('please enter 1,2, or 3')
                
    elif n==4:
            d_name = input("Whose details do you want to delete? ")
            if d_name in main_dict.keys():
                while True:
                    choice2 = int(input("\n1.name \n2.Address \n3.phone number \n4.email \n5.exit\nchoose what do you want to delete: "))
                    if choice2 == 1:
                        z = main_dict.pop(d_name)
                        print(d_name,"is removed from the phonebook")
                        print(main_dict)
                        break

                    elif choice2 == 2:
                        y = main_dict[d_name].pop("address")
                        print(main_dict)

                    elif choice2 == 3:
                        ch = input("Delete all numbers? y or n ")
                        if ch == 'y':
                            del main_dict[d_name]["phonenumber"]
                            print(main_dict)
                        elif ch == 'n':
                            ph_pos = int(input("Enter the position of number which you want to delete "))
                            del main_dict[d_name]["phonenumber"][ph_pos-1]
                            print(main_dict)

                    elif choice2 == 4:
                        ch = input("Delete all emails? y or n ")
                        if ch == 'y':
                            del main_dict[d_name]["email"]
                            print(main_dict)
                        elif ch == 'n':
                            email_pos = int(input("Enter the position of email which you want to delete "))
                            del main_dict[d_name]["email"][email_pos-1]
                            print(main_dict)

                    elif  choice2 == 5:
                        break

                    else:
                        print("Enter the numbers in option(1 to 5)")
            else:
                print("Name not found")
        
    elif n == 5:
        break

    else:
        print("Not valid- Number not in choice")

                    


                


   