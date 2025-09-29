#LetterFrequency.py
#Name:
#Date:
#Assignment:

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0] * 26  # Initialize frequency list for each letter A-Z

    # Count each letter's frequency
    for letter in message:
        if letter in alpha:
            index = alpha.find(letter)
            freq[index] += 1

    # Create output text in format A,5\n
    output = ""
    for i in range(26):
        print(alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output += line

    writeToFile(output)

def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    with open("frq.csv", 'w') as freqFile:
        freqFile.write(fileText)

def main():
    msg = input("Enter a message: ")
    countLetters(msg)

if __name__ == '__main__':
    main()
