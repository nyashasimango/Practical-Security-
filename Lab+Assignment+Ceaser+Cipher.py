
# coding: utf-8

# In[4]:

#Function to encrypt
def encrypt(a,b):
    h=int(a)
    i=int(b)
    result=((i+h)%26)
    return result
#Function to decrypt
def decrypt(a,b):
    h=int(a)
    i=int(b)
    result=((i-h)%26)
    return result
#Function to start execution
def calculate():
    x=3
    v= int(input("select (1.) To encrypt (2.) To encrypt  (3.) To exit   :")) 
    
    if(v==1):
        z=input("input string to encrypt :")
        for words in z:
            g=convert(words)
            answer=encrypt(x,g)
            final=converts(answer)
            print(final,end='')
            
    elif(v==2):
        z=input("input string to decrypt :")
        for words in z:
            g=convert(words)
            answer=decrypt(x,g)
            final=converts(answer)
            print(final,end='')
    
    else:
        print("about to exit")
    
#Function to convert a letter to int equiv    
def convert(letter):
    
    if (letter=="a" or letter=="A" ):
        equiv=0
    elif (letter=="b" or letter=="B" ):
        equiv=1
    elif (letter=="c" or letter=="C" ):
        equiv=2
    elif (letter=="d" or letter=="D" ):
        equiv=3
    elif (letter=="e" or letter=="E" ):
        equiv=4
    elif (letter=="f" or letter=="F" ):
        equiv=5
    elif (letter=="g" or letter=="G" ):
        equiv=6
    elif (letter=="h" or letter=="H" ):
        equiv=7
    elif (letter=="i" or letter=="I" ):
        equiv=8
    elif (letter=="j" or letter=="J" ):
        equiv=9
    elif (letter=="k" or letter=="K" ):
        equiv=10
    elif (letter=="l" or letter=="L" ):
        equiv=11
    elif (letter=="m" or letter=="M" ):
        equiv=12
    elif (letter=="n" or letter=="N" ):
        equiv=13
    elif (letter=="o" or letter=="O" ):
        equiv=14
    elif (letter=="p" or letter=="P" ):
        equiv=15
    elif (letter=="q" or letter=="Q" ):
        equiv=16
    elif (letter=="r" or letter=="R" ):
        equiv=17
    elif (letter=="s" or letter=="S" ):
        equiv=18
    elif (letter=="t" or letter=="T" ):
        equiv=19
    elif (letter=="u" or letter=="U" ):
        equiv=20
    elif (letter=="v" or letter=="V" ):
        equiv=21
    elif (letter=="w" or letter=="W" ):
        equiv=22
    elif (letter=="x" or letter=="X" ):
        equiv=23
    elif (letter=="y" or letter=="Y" ):
        equiv=24
    elif (letter=="z" or letter=="Z" ):
        equiv=25
    else:
        print("letter not found in the Z26 universe")
        
    return equiv
#Function to convert an int to letter equiv  
def converts(equiv):
    
    if (equiv==0):
        letter="a" 
    elif (equiv==1):
        letter="b" 
    elif (equiv==2):
        letter="c" 
    elif (equiv==3):
        letter="d" 
    elif (equiv==4):
        letter="e" 
    elif (equiv==5):
        letter="f" 
    elif (equiv==6):
        letter="g" 
    elif (equiv==7):
        letter="h" 
    elif (equiv==8):
        letter="i" 
    elif (equiv==9):
        letter="j" 
    elif  (equiv==10):
        letter="k" 
    elif (equiv==11):
        letter="l" 
    elif (equiv==12):
        letter="m" 
    elif (equiv==13):
        letter="n" 
    elif (equiv==14):
        letter="o" 
    elif (equiv==15):
        letter="p" 
    elif (equiv==16):
        letter="q" 
    elif (equiv==17):
        letter="r" 
    elif (equiv==18):
        letter="s" 
    elif (equiv==19):
        letter="t" 
    elif (equiv==20):
        letter="u" 
    elif (equiv==21):
        letter="v" 
    elif (equiv==22):
        letter="w" 
    elif (equiv==23):
        letter="x" 
    elif (equiv==24):
        letter="y" 
    elif (equiv==25):
        letter="z" 
    else:
        print("about to exit hee")
    return letter
calculate()


# In[ ]:




# In[ ]:



