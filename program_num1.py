'''
Program 1:
Create a program that ask user for personal information. Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc. Write the collected information in a txt file. It's up to you on how you'd like to format the information in the file. The program should ask user if want to input another person or exit.
'''

name = input("What is your Name? ")

while True:    
    age = int(input("How old are you? "))
    if len(str(age)) <= 2:
        break
    else: 
        len(str(age)) >= 2
        print(" Please Input Two Digit Number! ")

birthday = (input("When is your birthday? "))
address = input("Which City and Province do you live in? ")
course = input("What course are you studying currently? ")

while True: 
    pet = input("Do you have a pet?(y/n) ")
    if pet == "y":
        pet_type = input("What type of Pet? ")
        break
    else: 
        pet != "y"    
        break

while True:
    hobby = input("Do you have a hobby?(y/n) ")
    if hobby == "y":
        hobby_kind = input("What kind of Hobby? ")
        break
    else: 
        hobby != "y"
        break

print("Thank you for answering! <3 ")