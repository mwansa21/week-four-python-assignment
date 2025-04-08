def read_and_modify_file():
    # Ask the user to enter the filename
    filename = input("Enter the filename to read from: ")

    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            contents = file.read()

        # Modify the content - let's make everything uppercase as an example
        modified_contents = contents.upper()

        # Create a new file to save the modified content
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_contents)

        print(f"\n File has been modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: There was a problem reading or writing the file.")

# Run the function
read_and_modify_file()
