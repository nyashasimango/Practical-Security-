
# coding: utf-8

# In[29]:

#this program uses Natural Language Toolkit Word_Tokenise function, to download this module type nltk.download() and run

#importing modules from AppData
import nltk
from nltk import word_tokenize

#taking user input
words=input("Input String :")

#Tokenising list of strings 
tokens=[]
tokens=word_tokenize(words)
size=1

for x in tokens:
    print(x, end='  ')
    print(len(x))
    if (size<len(x)):
        size=len(x)
        answer=x
print("The longest string is :",answer,"with length :" ,size)
    


# In[ ]:




# In[ ]:



