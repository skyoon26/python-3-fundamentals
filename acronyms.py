# 1. Ask for user input
look_up = input("What software acronym would you like to look up?\n")

found = False
# 2. Open the file
# The open() function returns a File object that has methods like read() and write()
# The with keyword makes sure the File is properly closed when the file operations are done even if an exception is raised
# The long way to close a File is using a try/finally block using close()
with open("acronyms.txt") as file:
    # The read() method returns the whole file as a String by default or a specified number of bytes
    # The readline() method returns the next line of the file as a String
    # The readlines() method return a list of Strings of all of the lines in the file
    # We can loop over this list and print each line
    # Example:
    # result = file.readlines()
    # for line in result:
    #     print(line)

    # 3. Read each line of the file
    # This is the shortcut to loop over the File object:
    for line in file:
        # 4. Check if the user's input matches the current acronym
        if look_up in line:
            # 4. Print the definition
            print(line)
            found = True
            break

if not found:
    print("The acronym does not exist")
