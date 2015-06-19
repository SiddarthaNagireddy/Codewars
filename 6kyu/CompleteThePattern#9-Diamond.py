'''
Created on Jun 19, 2015

@author: Siddartha Reddy
'''


''' 

pattern(5):


    1    
   121   
  12321  
 1234321 
123454321
 1234321 
  12321  
   121   
    1  
    

'''

def line(n,maxlen):
    s=""
    pad=" " * (maxlen - n)
    s=pad
    for i in range(n):
        s += str((i+1)%10)


    for i in reversed(range(n-1)):
        s += str((i+1)%10)
    return s+pad


def pattern(n):
    # Happy Coding ^_^
    if n<=0 : return ""
    s=""
    for i in range(n):
        s += line(i+1,n)
        if n > 1:
            s += "\n"


    for i in reversed(range(n-1)):
        s += line(i+1,n)
        if i > 0:
            s += "\n"

    return s
    
print pattern(5)