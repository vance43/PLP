filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as infile:
        content = infile.read()
    
        modified_content = content.upper()

    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)
    print(f"Modified content written to {new_filename}")

except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read or write to the file.")
