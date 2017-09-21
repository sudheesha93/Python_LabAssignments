# Python program that accepts a sentence as input and remove duplicate words.
# Sort them alphanumerically and print it.


sentence= input('Enter the input sentence: ')              # Taking the sentence as input
words = sentence.split()                              # Splitting the sentence into words
words = [element.lower() for element in words]         # converting all the words to lowercase

a=set(words)                                            # Converting the words into set
b=set()                                                 # defining an empty set
result = []                                             # defining an empty list
for item in a:
    if item not in b:
        b.add(item)
        result.append(item)                             # appending the unique items into the list
res=sorted(result)                                      # sorting the list alphanumerically
print(' '.join(word for word in res))

