import sys

buffer = ""

print("Welcome to Virgil!")
print("Please enter user name:")
while input() != "user1":
    input("User does not exit! Please try again!\n")

else:
    print("Welcome back user1!\nYou can tpye whatever you need below!")
    try:
        while True:
            input()
            userInput = input()
            buffer += userInput + "\n"
    except:
        sys.exit()
