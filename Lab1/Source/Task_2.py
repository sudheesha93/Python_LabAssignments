# Program to check if a given string contain all the 26 alphabets
import string

str = input("Enter an input string: ")                # String input from the user

alphastring = set(string.ascii_lowercase)                  # creating a default set which contains all the 26 alphabets in lowercase

if set(str.lower()) >= alphastring:                   # condition for checking whether the input string has all the alphabets
    print ("\n The string "+str+ " contains all the 26 alphabets")
else:
    print("\n The string does'nt have all the alphabets")