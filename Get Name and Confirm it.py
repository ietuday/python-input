# Getting user name
name=input("Type Your Name \n")
#Confirming user name
cnfrm=input(f"You are Confirm your name is {name}\nif Yes then Type [Yes] if Wrong then Type [No]\n")
cnfrm=cnfrm.lower()
#For Confrim to match inputs
Yes="yes"
No="no"
#Putting Condition to Confirmation
if (cnfrm==Yes):
    print("Thanks for Processing")
#in Condition putting loop if Confirmation reply with No
elif(cnfrm==No):
    while cnfrm==No:
        name=input("Again Type your Name ")
        cnfrm=input(f"You are Confirm your name is {name}\n if Yes then Type [Yes] if Wrong then Type [No]\n")
        cnfrm=cnfrm.lower()
# while loop if condition true then break and printing
        if (cnfrm==Yes):
            print("Thanks for Processing")
            break
#if user confirmation reply is wrong then we go in else
else:
    print("Your Confirmation is Wrong Reload page")