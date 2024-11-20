[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zqG4OtSz)
<h1>CS151 Lab 11</h1>

 <h3>🔴 DO NOT Start to code before the instructor Approve your algorithm, and test cases🔴</h3>

- **Grade: EMRN**
- **Due: Before Next Lab**

<h3>Table of contents</h3>

<!-- TOC -->
  * [`Problem`](#problem)
  * [`Purpose`](#purpose)
  * [`Details`](#details)
  * [`Design`](#design)
  * [`Steps`](#steps)
  * [`Programming Hints`](#programming-hints)
  * [`What to Submit in GitHub`](#what-to-submit-in-github)
    * [Check List Before Submission](#check-list-before-submission)
<!-- TOC -->

## `Problem`
Someone has converted your files using a cipher! 
- Ciphers have been very popular for millenia as a way to hide information. 
- Can you create a program to convert them back to plain English??

## `Purpose`
This lab gives you practice with: 
* Using dictionaries
* Following problem-solving techniques
* Creating functions
* Doing file I/O

## `Details`
Morse code is a code for representing letters such that it can be communicated via blinking lights or sounds. 
- There are only 2 symbols: `dots (.) and dashes (-)`. 
- A specific ordering of dots and dashes represents a particular letter, number, or symbol. 
- You can see an example of morse code as a communication signal at [YouTube Here](https://www.youtube.com/watch?v=_J8YcQETyTw&ab_channel=DaveHimslef).

Open your `morsecode.txt` file to see the conversions. 
- You have all English letters, the digits of base 10, and a few punctuation symbols. 
- This file tells you how to convert between Morse code and English, with a *tab* between the two columns.

The files you must convert are written in Morse Code with a space between the letters, with one word per line.

## `Design`
**For this lab you MUST use iterative development. <br> You must work on your algorithms in a specific order. See the Steps, and FOLLOW them.** 

- Your program will first read in `morsecode.txt` to learn the conversions
  - Think about the best way (suitable data structure) to store this information.
- Next it will ask the user for the name of a file that is written in Morse code, convert it to English. 
  - The program then writes the English conversion out on to a NEW file (The file name for the output is chosen by user).
  - 🟢`N.B. It is possible to read from one file and write onto another file from a single function`🟢
    - Imagine as if you are copying from one file and pasting onto another
- Your program MUST ask for the following information from the user: 
  - the name of your file that shows the conversions (e.g. `moresecode.txt` in this case), 
  - the name of the input file that is written in morse code, and 
  - the name of the output file. 

## `Steps`
**Take turns driving by function.** Every time you move to a new function, change who is typing. 
- Just move the keyboard over, you don't need to swap seats.

1. Make sure you understand the problem
2. Design: 
   - You will need functions to do: 
     - file name input error checking, 
     - storing conversion information from morsecode.txt, 
     - reading in the morse code text, 
     - converting from morse to English and writing that conversion to a file, and 
     - main. 
   - For the design phase, you need to determine the:
     - Purpose
     - Name
     - Parameters, 
     - return types, and 
     - general approach for each function (including the data structure to use). 
       - 🟢`A full algorithm is not required.`🟢
   - *You should not need more than 15 minutes for the design step.* 
      - Ask questions if you get stuck! 
      - **Show the professor your design.** 
4. Follow iterative development! 
   - Write one function at a time, updating main to call the functions as you go, getting it to work before moving on. 
   - First should be file name input, and then reading in morsecode.txt and storing appropriately for later use. 
   - **switch drivers between functions**
5. Put output in main to test that your function to store you conversion from morsecode to letters is correct. 
   - You can delete this output once you've determined your code works so far.
6. Next write the function for converting a file written in morsecode to a file written in English. 
   - Test it to see that it works.
7. Write comments in your code to make it clear what it is doing.
8. Write comments for each function in your code. 
9. Include an updated version of the header comments. 
   - Be sure to note that you need input files in the "Other files" part! 

## `Programming Hints`
The code for this assignment is fairly short, but there are a few little things that might trip you up when you go to code your algorithm. 

Here are a few hints to help with that issue:
* Be careful how you name the variables in your for loops. 
  * Meaningful naming will make coding it correctly a LOT easier.
* The letter and morse code value in the file are separated by a tab. 
  * A tab is just another form of whitespace.
* You will need to strip both the key and the value after reading it from the file to remove whitespace. 
  * Otherwise, your code won’t be able to find the answer correctly.


## `What to Submit in GitHub`

1. Completed `main.py` file  
2. `algorithm.md`
3. Encrypt your files using the `keys` and `process_reflection.py`
   1. `RD1.md` -> Reflection for Drive 1
   2. `RD2.md` -> Reflection for Drive 2
   3. If you use a different key, it is considered unsubmitted

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get?
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?

### Check List Before Submission

- Asks the user for an input file name that contains conversion from morse code to english
- Asks user to try again if input file name doesn't exist (try bbb.txt)
- Asks user for name of input file to convert
- Asks user to try again if this files doesn't exist as well
- Asks user for name of output file, without error checking name
- Output file as converted text in it that makes sense (even if there are extra line breaks)
- Output file has space between words and no space between characters between words (not required, but helps earn an E)


- Error checking on user input is while os.path.isfile(filename) with filename being user input that is updated within the loop
- There is a function for error checking file name that returns file name
- There is a function for reading from the file that returns a list of lists
- There is a function for reading from initial file that returns a dictionary with keys as 2nd item on line, and values a 1st item
- Either another function writes to a file and does conversion, or the function that reads in file to convert also writes to file
- There are complete intro comments
- There are comments above each function (purpose, parameters, return info)


**Make sure the file in your PyCharm and Github is the same (i.e. Commit and Push)**