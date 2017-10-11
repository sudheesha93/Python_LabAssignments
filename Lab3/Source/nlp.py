
from __future__ import division
import nltk, re, pprint
import re, collections

data_path='C:/Users/sudheesha/Documents/GitHub/Python_LabAssignments/Lab3/Source/data/'
f=open(data_path+'sample_text.txt')
raw=f.read().lower()
f=open(data_path+'sample_text.txt')
raw_lines=f.readlines()

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(raw)

# lemmatization
wnl = nltk.WordNetLemmatizer()
lem_txt=[wnl.lemmatize(t) for t in tokens]
print('Lemmatization')
print(lem_txt)
print('----------------------------------------------------------')

# pos tagging
pos_txt=nltk.pos_tag(tokens)
print('After applying POS')
print(pos_txt)
print('------------------------------------------------------------------------')


verbs=[s[0] for s in pos_txt if s[1] == 'VB']
remaining_words=[s[0] for s in pos_txt if s[1] != 'VB']

# removing stop words such as 'the','is'
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

filtered_words = [w for w in remaining_words if not w in stop_words]
print('After removing all the verbs')
print(filtered_words)
print('--------------------------------------------------------------------------')


# Calculate frequency distribution of the filtered words
fdist = nltk.FreqDist(filtered_words)
words=[s[0] for s in fdist.most_common(50)]
freq=[s[1] for s in fdist.most_common(50)]

WordCount = collections.Counter(filtered_words)
print('Frequency count os the words from the filtered list')
print(WordCount)
print('---------------------------------------------------------')

# Top5Words = WordCount.most_common(5)
# TopWords = [word for (word,freq) in Top5Words]

# top 5 words in the text
top_5_words=words[:5]
print("To display the top 5 words")
print(top_5_words)
print('-----------------------------------------------------------------------------')

# filtering the sentences with those most repeated words
rep_sen=[]
for i in top_5_words:
    for j in raw_lines:
        if i in j:
            rep_sen.append(j)
print('Extrating the sentences with most repeated words')
print(rep_sen)
print('---------------------------------------------------------------------------------------')

# Extracting , concatinating and exporting to a text file
file = open(data_path+'top_5_word_lines.txt','w') 
for i in rep_sen:
    file.write(i)
file.close() 
