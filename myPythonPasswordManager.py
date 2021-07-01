import os.path
def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt","w")
        file.close()

def appendNow():
    file = open("info.txt",'a')
    print()
    print()
    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Pleaseenter the website address here: ")
    print()
    print()
    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"
    file.write("--------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("--------------------------------\n")
    file.write("\n")
    file.close()

def readPasswords():
    file = open("info.txt","r")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()
    
response = input("Would you like to enter passwords for your website(s) with this application? (y/n): ")
while(str(response) != 'y' and str(response) != 'n'):
    print("Sorry, but the response you have given is invalid. Please try again.")
    response = input("Would you like to enter passwords for your website(s) with this application? (y/n): ")
if(response == "y"):
    checkExistence()
    while(True):
        appendNow()
        continueResponse = input("Would you like to continue entering passwords for your website(s) with this application?(y/n): ")
        while(str(continueResponse) != 'y' and str(continueResponse) != 'n'):
            print("Sorry, but the response you have given is invalid. Please try again.")
            continueResponse = input("Would you like to continue entering passwords for your websites(w) with this application? (y/n): ")
        if(continueResponse == 'n'):
            break
        elif(continueResponse == 'y'):
            continue
    doReadPasswords = input("Would you like for each of your passwords to your website(s) to be read back to you? (y/n): ")

    while(str(doReadPasswords) != 'y' and str(doReadPasswords) != 'n'):
        print("Sorry, but the response you have given is invalid. Please try again.")
        doReadPasswords = input("Would you like for each of your passwords to your website(s) to be read back to you? (y/n): ")

    if(doReadPasswords == 'y'):
        readPasswords()
else:
    print("Sorry to hear that.")
    print("Execute this program again if you would like to use it to store the password(s) to your website(s).")

