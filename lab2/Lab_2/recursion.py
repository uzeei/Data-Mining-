#Lab 2: Recursion
def recursion_factorial(x):
    print(x,'test')
    if x<0:
        
        return "Please enter only positive integers"
    
    elif x==0 or x==1:
        return 1
    else:
        
        return x*recursion_factorial(x-1)
        
print(recursion_factorial(5))
print(recursion_factorial(0))

#HW Task 1: Implement Fibonacci squence using recursion: 
'''
Your program should take an input number 'n' and generate first 'n' Fibonacchi numbers.
For e.g if user wants first '7' fibonacchi numbers then it should print:

0,1,1,2,3,5,8
'''

