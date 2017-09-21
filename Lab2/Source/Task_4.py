# Using Numpy creating a random vector of size 15 and replace the maximum value by 100

import numpy as np              # Importing the libraries
vector = np.random.rand(15)     # Creating a random vector of size 15
print('Vector with random values of size 15 \n')           # Printing the vector

print(vector)
vector[vector.argmax()] = 100               # replacing the max value in the vector with 100
print('\n Vector after replacing the maximum value with 100 is below \n ')            # Printing the newly generated vector
print(vector)
