# Algorithm for Morse Code Decoder Program

---

### Algorithm for `get_valid_filename`
- **Purpose**: Prompt user for a valid filename with error checking.
- **Name**: `get_valid_filename`
- **Parameters**: `prompt` (string) - The message to display for input.
- **Return**: A valid filename as a string.
- **Algorithm**:
  1. Prompt the user for a filename using the given `prompt`.
  2. While the file does not exist:
     1. Display an error message: "Error: File does not exist. Please try again."
     2. Prompt the user for the filename again.
  3. Return the valid filename.

---

### Algorithm for `read_morse_code_dictionary`
- **Purpose**: Read the Morse code dictionary from the file.
- **Name**: `read_morse_code_dictionary`
- **Parameters**: `filename` (string) - The Morse code dictionary file.
- **Return**: A dictionary with Morse code as keys and English letters/numbers as values.
- **Algorithm**:
  1. Create an empty dictionary `morse_dict`.
  2. Open the file with the given `filename` in read mode.
  3. For each line in the file:
     1. Remove extra spaces using `strip()`.
     2. Split the line into `values` based on the delimiter `'  '` (double spaces).
     3. Create `key` from the second value
     4. Create `value` from the first value
     5. Update `morse_dict` using the `key-value` pair
  4. Return `morse_dict`.

---

### Algorithm for `read_morse_code_file`
- **Purpose**: Read the Morse code text file to decode.
- **Name**: `read_morse_code_file`
- **Parameters**: `filename` (string) - The file containing Morse code.
- **Return**: A table (list of lists) where each row is a list of Morse code sequences.
- **Algorithm**:
  1. Create an empty list `table`.
  2. Open the file with the given `filename` in read mode.
  3. For each line in the file:
     1. Remove extra spaces using `strip()`.
     2. Split the line into words using a single space (`' '`) and append the resulting list to `table`.
  4. Return `table`.

---

### Algorithm for `decode_morse_row`
- **Purpose**: Decode a row of Morse code using the dictionary.
- **Name**: `decode_morse_row`
- **Parameters**:
  - `row` (list of strings) - A list of Morse code sequences in a single line.
  - `morse_dict` (dictionary) - The Morse code dictionary.
- **Return**: The decoded English string.
- **Algorithm**:
  1. Create an empty string `decoded_line`.
  2. For each `word` in the `row`:
     1. Use the `morse_dict` to get the English equivalent of `word`.
     2. Append the English letter to `decoded_line`.
  3. Return `decoded_line`.

---

### Algorithm for `decode_morse_to_file`
- **Purpose**: Decode the entire Morse code text and write it to an output file.
- **Name**: `decode_morse_to_file`
- **Parameters**:
  - `table` (list of lists) - Morse code rows to decode.
  - `morse_dict` (dictionary) - The Morse code dictionary.
  - `output_file` (string) - The name of the output file.
- **Return**: None.
- **Algorithm**:
  1. Open the `output_file` in write mode.
  2. For each `row` in `table`:
     1. Decode the `row` using `decode_morse_row` with `morse_dict`.
     2. Write the decoded line to the `output_file` followed by a newline character.
  3. Close the file.

---

### Algorithm for `main`
- **Purpose**: Main function to drive the Morse code decoder program.
- **Name**: `main`
- **Parameters**: None.
- **Return**: None.
- **Algorithm**:
  1. Display a welcome message: "Welcome to the Morse Code Decoder!"
  2. Prompt the user for the Morse code dictionary file using `get_valid_filename`.
  3. Read the Morse code dictionary using `read_morse_code_dictionary`.
  4. Prompt the user for the input Morse code file using `get_valid_filename`.
  5. Read the Morse code lines and create a table using `read_morse_code_file`.
  6. Prompt the user for the output file name.
  7. Decode the Morse code table and write the output to the file using `decode_morse_to_file`.
  8. Display a success message: "Decoding complete! The decoded text has been saved to 'output_file'."

