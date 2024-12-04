import os

# Function to load Morse code mappings from file
# Parameters:
#   filename: The file containing Morse code mappings.
# Returns: A dictionary with Morse code as keys and English letters as values.
def load_morse_mapping(filename):
    morse_mapping = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                char, morse = line.strip().split("\t")
                morse_mapping[morse] = char
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit()
    return morse_mapping

# Function to prompt the user for a valid file name.
# Parameters:
#   prompt: The prompt to display to the user.
# Returns: A valid file name provided by the user.
def error_check_filename(prompt, options):
    print(f"Available files: {', '.join(options)}")
    filename = input(prompt)
    while filename not in options or not os.path.isfile(filename):
        print(f"Error: {filename} is not a valid option. Try again.")
        filename = input(prompt)
    return filename

# Function to read Morse code from a file.
# Parameters:
#   filename: The name of the file containing Morse code.
# Returns: A list of lines (each line is a string of Morse code).
def read_morse_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit()

# Function to write the converted text to a file.
# Parameters:
#   filename: The name of the output file.
#   text: The text to write to the file.
def write_output_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

# Function to convert Morse code into plain text.
# Parameters:
#   morse_lines: A list of lines of Morse code.
#   morse_mapping: A dictionary mapping Morse code to letters.
# Returns:The decoded plain text.
def convert_morse_to_text(morse_lines, morse_mapping):
    decoded_text = ""
    for line in morse_lines:
        words = line.strip().split(" ")  # Split Morse code letters by space
        for morse_char in words:
            if morse_char in morse_mapping:
                decoded_text += morse_mapping[morse_char]
            else:
                decoded_text += "?"  # Placeholder for unknown Morse code just in case
        decoded_text += " "  # Space between words
    return decoded_text.strip()

# Main program
def main():
    # Load Morse code mappings
    morse_mapping_file = error_check_filename(
        "Enter the Morse code mapping file (e.g., morsecode.txt): ",
        ["morsecode.txt"]
    )
    morse_mapping = load_morse_mapping(morse_mapping_file)

    # Get the input Morse code
    morse_files = ["morse1.txt", "morse2.txt", "morse3.txt"]
    input_file = error_check_filename(
        "Enter the name of the Morse code file to convert (e.g., morse1.txt): ",
        morse_files
    )

    # Read the Morse code
    morse_lines = read_morse_file(input_file)

    # Convert Morse code to plain text
    decoded_text = convert_morse_to_text(morse_lines, morse_mapping)

    # Get the output file name
    output_file = input("Enter the name of the output file (e.g., output.txt): ")
    write_output_file(output_file, decoded_text)
    print(f"Conversion completed! Decoded text has been written to {output_file}")

# Run the program
if __name__ == "__main__":
    main()
