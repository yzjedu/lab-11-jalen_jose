
- [LAB-11 Feedback](#lab-11-feedback)
    - [Test Cases](#test-cases)
    - [Blind Test: Running the code](#blind-test-running-the-code)
    - [Open Test: Looking at the code](#open-test-looking-at-the-code)
    - [Documents for Participation Grade](#documents-for-participation-grade)
    - [Comments on the grading](#comments-on-the-grading)
    - [Grade:](#grade)
    - [Participation Grade:](#participation-grade)


# LAB-11 Feedback

### Test Cases

| Test Case | in: morse_file_name | in: input_file_name| in: out_file_name | in: out_file_name                  |
|-----------|---------------------|--------------------|-------------------|------------------------------------|
| 1         | bbb.txt             | try again          |                   |                                    |
| 2         | morsecode.txt       | bbb.txt            |                   | try again                          |
| 3         | morsecode.txt       | morse1.txt         | decoded1.txt      | decoded1.txt start with `MR.`      |
| 4         | morsecode.txt       | morse2.txt         | decoded2.txt      | decoded2.txt start with `FOUR`     |
| 5         | morsecode.txt       | morse3.txt         | decoded2.txt      | decoded2.txt start with `WHEN,`    |

    
### Blind Test: Running the code
| Result       | Description                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------|
| **YES-NO**   | Asks the user for an input file name that contains conversion from morse code to English                           |
| **YES-NO**   | Asks user to try again if input file name doesn't exist (try `bbb.txt`)                                             |
| **YES-NO**   | Asks user for name of input file to convert                                                                         |
| **YES-NO**   | Asks user to try again if this file doesn't exist as well                                                           |
| **YES-NO**   | Asks user for name of output file, without error checking name                                                      |
| **YES-NO**   | Output file has converted text in it that makes sense (even if there are extra line breaks)                         |
| **YES-NO**   | Output file has space between words and no space between characters in words (not required, but helps earn an E)    |

### Open Test: Looking at the code
| Result       | Description                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------|
| **YES-NO**   | The algorithm matches the code                                           |
| **YES-NO**   | Purpose of the program is clearly stated                                   |  
| **YES-NO**   | Error checking on user input is `while os.path.isfile(filename)` with filename being user input that is updated within the loop |
| **YES-NO**   | There is a function for error checking file name that returns file name                                             |
| **YES-NO**   | There is a function for reading from initial file that returns a dictionary with keys as 2nd item on line, and values as 1st item |
| **YES-NO**   | There is a function for reading from the file that returns a list of lists                                          |
| **YES-NO**   | Either another function writes to a file and does conversion, or the function that reads in file to convert also writes to file |
| **YES-NO**   | There are complete intro comments                                                                                   |
| **YES-NO**   | There are comments above each function (purpose, parameters, return info)                                           |



### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**YES-NO** | Reflection 1   |
|**YES-NO** | Reflection 2   |
|**YES-NO** | Algorithm      |

### Comments on the grading
- There is nothing to grade here
- 
- 

### Grade: N

### Participation Grade: U
 - If participation grade is unsatisfactory check the `NO` in the documents sections