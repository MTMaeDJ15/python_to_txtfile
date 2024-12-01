''' 
Program 2:
Create another program that ask user for fullname. Find the full name in the txt file (output of program1). Display the informations found in the txt file.
'''
def search_in_file():
    name_to_search = input("Enter the Name(Sn, Fn M.I) of the person you want to find: ")

    with open("./python_to_txtfile.txt", "r") as file_handle:
        print(f"\nSearching for '{name_to_search}' in the file...")
        lines = file_handle.readlines()

search_in_file()