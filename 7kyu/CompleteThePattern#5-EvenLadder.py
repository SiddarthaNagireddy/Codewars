'''
Created on Jun 18, 2015

@author: Siddartha Reddy
'''

''' 

pattern(8):

22
4444
666666
88888888

pattern(5):

22
4444

'''

def pattern(n):
    return '\n'.join(str(x)*x for x in range(2,n+1,2))
    
print pattern(8)
print "\n \n"
print pattern(6)