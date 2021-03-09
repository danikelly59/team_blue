"""
CSE 5408
"""

def fibonacci(num):
    if (num <= 0):
        return 0
    
    fib = [0] * (num + 1)
    fib[1] = 1
    sm = fib[0] + fib[1]
    
    for i in range(2,num+1):
        fib[i] = fib[ i-1] + fib[i-2]
        sm = sm + fib[i]
        
    return sm

print("Please input a number")
num =int( input())
print("The Fibonacci sum is ", fibonacci(num))