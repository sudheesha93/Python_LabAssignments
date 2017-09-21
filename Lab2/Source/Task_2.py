# Python program to generate a dictionary that contains (k, k*k).
# And printing the dictionary that is generated including both 1 and k.




number = input("Input a number ")              # Taking the input number
n=int(number)
dictionary = dict()                                  # Initialising the dictionary

for k in range(1,n+1):                              # Calculating the k*k using a for loop
    dictionary[k] = k*k

print('Generated Dictionary (k,k*k) is ')                   # Printing the dictionary k,k*k

print(dictionary)

