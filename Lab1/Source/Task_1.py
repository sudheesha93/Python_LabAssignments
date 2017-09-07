# TO READ A TEXT FILE GIVEN BY THE USER
# TO CALCULATE THE FREQUENCY OF EACH WORD FROM THE FILE
# TO DISPLAY ALL WORDS WITH THEIR FREQUENCIES

freqwordcount= {}

# Opening the file in read-write mode

with open('../file.txt', 'r+') as file:                  # To read a file and assigning some name to the file
    for line in file:                                    # Split the file into lines
        for word in line.split():                            # Split the lines into words
            if word not in freqwordcount:                               # Check if the word is already present or not
                freqwordcount[word] = 1                                 # Calculate the frequency of each word
            else:
                freqwordcount[word] = freqwordcount[word]+1                                # If the word is already present increment the count by 1
    for i, j in freqwordcount.items():                   # To display allthe words in text file along with their frequency of occurences which is equal to the wordcount
        print(i, j)
file.close()