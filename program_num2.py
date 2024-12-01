''' 
Program 2:
Create another program that ask user for fullname. Find the full name in the txt file (output of program1). Display the informations found in the txt file.
'''
def search_in_file():
    name_to_search = input("Enter the Name of the person you want to find:(Sn, Fn M.I) ")
    found = False
    with open("./python_to_txtfile.txt", "r") as file_handle:
        print(f"\nSearching for '{name_to_search}' in the file...")
        lines = file_handle.readlines()

    for i in range(0, len(lines), 8):
        if name_to_search.lower() in lines[i].lower():
            found = True 
            print(f"\nInformation under '{name_to_search}': ")
            print("".join(lines[i:i+8]))
            break

    if not found: 
        print("Not Found!")

search_in_file() 