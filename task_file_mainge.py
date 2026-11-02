while True:


    print("choose 1 add student")
    print("choose 2 veiw student")
    print("choose 3 exit student")


    CHOICE=input("entr chooice")


    if CHOICE ==1:
        marks= input("enter your marks")
        name=input("enter a student nme ")


        with open ("student.txt","a") as file:
            file.write(name +  "-" +marks   )
            print("tuent added" )


    elif CHOICE ==2:
        with open ("student.txt","r") as file:
            print(file.read())


    elif CHOICE == 3:
        print("good bye")
        break


    elif CHOICE== 4:
        count=0
        with open("file.txt",'r') as f:
          print(len(f.readlines))
    else :
        print("invalid choice ")

