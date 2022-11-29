# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and structured data error handling
# ChangeLog (Who,When,What):
# Jonathan Kung, 11/26/2022, created script and code
# ---------------------------------------------------------------------------- #

# Script: Ask user for name and id number, then saves the list in binary format using pickling

import pickle

file_name = "Name_ID.txt"
data = []
name_id_list = []

try: # if no txt file is already created in the current folder, then the code will skip reading the data and continue to the next section of the code
    file = open(file_name, "rb") # 'rb' read txt file in binary format
    while(True):
        try: # load each line of data from the file into list
            data.append(pickle.load(file))
        except:
            break
    file.close()
    print("\n Current List: ")
    print(data, "\n")

except:
    pass

print('''\n Menu
1) Enter name/id
2) Save list
3) Exit
''')

while(True):
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = str(input("enter your name: "))
        id = int(input("enter your numerical id: "))
        data.append([name, id]) # add user inputs to the end of the current list
        print("\n Current List: ")
        print(data, "\n")
        continue
            
    elif choice == "2":
        print("\n Current List: ")
        print(data)
        file = open(file_name, "ab") # append data in binary format
        file_data = pickle.dump(data, file) # store data into txt file
        file.close()
        print("data has been saved. ")
        continue
        
    elif choice == "3":
        break








