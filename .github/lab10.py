#Programmers: Callie Walker, Lesdy Galvez
#Course: CS151, Dr. Rajeev
#Date: 12/2/21
#Lab Number: 10
#Program Inputs: The morse code file
#Program Outputs: print the list of morsecode as a dictionary
import string
def readfile(filename):
    letter_list = []
    try:
        file = open(filename, "r" )
        for line in file:
            temp = line.split( )
            if temp[0] != "-":
                for letter in temp:
                    letter = letter.lower().strip()
                    letter_list.append(letter)
    except FileNotFoundError:
        return []
    return letter_list
def separate_alphabet(list):
    letter_list = []
    i = 0
    for i in range (0, len(list), 2):
        letter = list[i]
        letter_list.append(letter)
    return letter_list
def separate_morse(list):
    morse_list = []
    i = 1
    for i in range(1, len(list), 2):
        m_code = list[i]
        morse_list.append(m_code)
    return morse_list
def dict(list1, list2):
    dictionary = { }
    for i in range (len(list2)):
        dictionary[list1[i]] = list2[i]
    return dictionary
def read_morse(data, dictionary):
    letter = dictionary.key()
    for morse in range(len(data)):
        if(letter == morse):
            return letter
def main():
    morse = readfile("morsecode.txt")
    #print(morse)
    alphabet = separate_alphabet(morse)
    morse_code_symbols = separate_morse(morse)
    morse_dictionary = dict(alphabet, morse_code_symbols)
    print(morse_dictionary)
    morse_to_decode = input("Enter a file name ")
    morse_file = readfile(morse_to_decode)
    #print(read_morse(morse_file, morse_dictionary))


main()

