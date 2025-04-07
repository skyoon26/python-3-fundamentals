def find_acronym():
    # Ask for user input
    look_up = input("What software acronym would you like to look up?\n")
    found = False
    try:
        # Open the file
        with open("acronyms.txt") as file:
            # Read each line of the file
            for line in file:
                # Check if the user's input matches the current acronym
                if look_up in line:
                    # Print the definition
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return

    if not found:
        print("The acronym does not exist")


def add_acronym():
    # Ask the user what acronym they want to add
    acronym = input("What acronym do you want to add?\n")
    # Then ask the user for the definition
    definition = input("What is the definition?\n")
    # Open the file
    with open("acronyms.txt", "a") as file:
        # Write the new acronym and definition to the file
        file.write(acronym + " - " + definition + "\n")


def main():
    # Ask the user whether they want to find or add an acronym
    choice = input("Do you want to find(F) or add(A) an acronym?\n")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()


main()
