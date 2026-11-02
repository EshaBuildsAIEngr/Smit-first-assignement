email="eshameo"
passward="12344"
def login():
    user_email= input("enter your email: ")
    user_passward=input("enter your passward :")
    if user_email == email:
        if user_passward == passward:
            print("succesful")
        else:
            print("wrong passward")
    else :
        print("wrong email")

login()





