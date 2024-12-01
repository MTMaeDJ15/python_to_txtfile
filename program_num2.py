''' 
Program 2:
Create another program that ask user for fullname. Find the full name in the txt file (output of program1). Display the informations found in the txt file.
'''
with open("./python_to_txtfile.txt", "r") as file_handle:
    lines = file_handle.readlines()
    for line in lines:
        print(line.strip())
