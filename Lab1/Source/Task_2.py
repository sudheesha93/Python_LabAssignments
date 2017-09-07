# Program to check if a given string contain all the 26 alphabets
import string

stringinput= input("Enter an input string: ")                       # String input from the user

alphastring = set(string.ascii_lowercase)                           # creating a default set which contains all the 26 alphabets in lowercase

print(" \n All the letters in the random order \n")
print(alphastring)

if set(stringinput.lower()) >= alphastring:                           # condition for checking whether the input string has all the alphabets
    print ("\n The string "+stringinput+ " contains all the 26 alphabets")
else:
    print("\n The string " +stringinput+ " does'nt have all the alphabets")