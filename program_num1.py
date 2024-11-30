'''
Program 1:
Create a program that ask user for personal information. Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc. Write the collected information in a txt file. It's up to you on how you'd like to format the information in the file. The program should ask user if want to input another person or exit.
'''

def data():
    information = [] 
    while True:
        name = input("What is your Name? ")
        while True:    
            age = int(input("How old are you? "))
            if len(str(age)) <= 2:
                break
            else: 
                len(str(age)) >= 2
                print(" Please Input a! ")

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

        information.append({
            "Name":name, 
            "Age":age, 
            "Birthday": birthday, 
            "Address":address, 
            "Course":course, 
            "Pet":pet_type, 
            "Hobby":hobby_kind
            })

        retry = input("Do you want to enter another set of data?(y/n) ").lower()

        if retry != "y": 
            break

    return information

def main():
    information = data()

    with open("./python_to_txtfile.txt","a") as file_handle: 
        for person in information:
            file_handle.write(f"Name: {person['Name']}\n")
            file_handle.write(f"Age: {person['Age']}\n")
            file_handle.write(f"Birthday: {person['Birthday']}\n")
            file_handle.write(f"Address: {person['Address']}\n")
            file_handle.write(f"Course: {person['Course']}\n")
            file_handle.write(f"Pet: {person['Pet']}\n")
            file_handle.write(f"Hobby: {person['Hobby']}\n")
            file_handle.write("-" * 30 + "\n")

    print("\nList of Information Entered:")
    for person in information:
        print(f"Name: {person['Name']}, Age: {person['Age']}, Birthday: {person['Birthday']}, Address: {person['Address']}, Course: {person['Course']}, Pet: {person['Pet']}, Hobby: {person['Hobby']}")

main()
