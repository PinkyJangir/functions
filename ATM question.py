print("Welcome to state bank of India")
print("Please insert your card")
language=input("1. English\n 2. Hindi\n 3. Marathi\n please select your language:  ")
if language=='1':
    print("English")
elif language=='2':
    print("Hindi")
elif language=='3':
    print("Marathi")
pin=int(input("enter your pin: "))
My_pin=1529
if pin==My_pin:
    pass
    Amt=5000
    transaction=input("Cash withdrawl\n balance enquery\n deposite\n change pin\n select your transaction: ")
    if transaction=="Cash withdrawl":
        Amount=int(input("enter an amount: "))
        if Amount<=Amt:
            print("Collect your cash") 
    elif transaction=="deposite":
        dep=int(input("enter an amount: "))
        if dep>0:
            print("successfully deposite")
        else:
            print("no cash")
    elif transaction=="change pin":
        old_pin=int(input("enter ur current pin:"))
        if old_pin==My_pin:
            new_pin=int(input("enter your new pin: "))
            My_pin=new_pin
            print("succesfully changed")
        else:
            print("incorrect current pin")
    elif transaction=="balance enquery":
        print(Amt)
        receipt=input("do you want receipt: ")
        if receipt=="yes":
            print("take your receipt")
        else:
            print("Thank you")    
else:
    print("incorrect Pin! Please try again")