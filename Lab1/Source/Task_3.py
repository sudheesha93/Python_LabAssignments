# Program to find the numbers which are divisible by 5 and multiple of 2, between 700 and 1700

# Creating a list to add all the numbers which satisfy the given condition

numbers = []

for i in range(700, 1700):                                      # range of the numbers is 700 to 1700
    if i%5 == 0 and i%2 == 0:                                  # Checking the condition- number divisible by 5 and also multiple of 2
        numbers.append(i)                                 # If the number satisfies the condition append that number to the list

print("The numbers between 700 and 1700 that are divisible by 5 & also multiple of 2 are: \n")
print(numbers)                                                  # Dispaly all numbers from the list

