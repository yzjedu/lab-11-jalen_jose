# Programmers:  [your names here]
# Course:  CS151, [Instructors Name]
# Due Date: [date assignment is due]
# Lab Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Input Files: [description of the format of the input files you need for this program to work]


import os

# Purpose: Prompt user for a valid filename with error checking.
# Parameters: prompt (string) - The message to display for input.
# Returns: A valid filename as a string.
def get_valid_filename(prompt):
    filename = input(prompt).strip()
    while not os.path.isfile(filename):
        print("Error: File does not exist. Please try again.")
        filename = input(prompt).strip()
    return filename

# Purpose: Read the Morse code dictionary from the file.
# Parameters: filename (string) - The Morse code dictionary file.
# Returns: A dictionary with Morse code as keys and English letters/numbers as values.
def read_morse_code_dictionary(filename):
    morse_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            values = line.split('  ')
            key = values[1]
            value = values[0]
            morse_dict[key] = value
    return morse_dict

# Purpose: Read the Morse code text file to decode.
# Parameters: filename (string) - The file containing Morse code.
# Returns: A table of Morse code lists.
def read_morse_code_file(filename):
    table = []
    with open(filename, 'r') as file:
        for line in file:
            table.append(line.strip().split())
        return table

# Purpose: Decode a line of Morse code using the dictionary.
# Parameters: row (list) - A list of Morse code, morse_dict (dictionary).
# Returns: The decoded English string.
def decode_morse_row(row, morse_dict):
    #words = line.split(' ')  # Split the line into Morse code letters
    decoded_line = ''
    for word in row:
        decoded_line += morse_dict[word]
    return decoded_line

# Purpose: Decode the entire Morse code text and write to an output file.
# Parameters: table (list of lists), morse_dict (dictionary), output_file (string).
# Returns: None
def decode_morse_to_file(table, morse_dict, output_file):
    with open(output_file, 'w') as file:
        for row in table:
            decoded_line = decode_morse_row(row, morse_dict)
            file.write(decoded_line + '\n')

# Purpose: Main function to drive the Morse code decoder program.
# Parameters: None
# Returns: None
def main():
    print("Welcome to the Morse Code Decoder!")
    print("----------------------------------")

    # Step 1: Get the Morse code dictionary file
    morse_file = get_valid_filename("Enter the name of the Morse code dictionary file: ")

    # Step 2: Read the Morse code dictionary
    morse_dict = read_morse_code_dictionary(morse_file)

    # Step 3: Get the input Morse code file
    input_file = get_valid_filename("Enter the name of the file to decode: ")

    # Step 4: Read the Morse code lines and create table
    table = read_morse_code_file(input_file)

    # Step 5: Get the output file name
    output_file = input("Enter the name of the output file: ").strip()

    # Step 6: Decode and write the output
    decode_morse_to_file(table, morse_dict, output_file)

    print(f"Decoding complete! The decoded text has been saved to '{output_file}'.")

# Run the program
main()