def factorial(n):
    if n==0:
        return 1
    return factorial(n-1)*n

num = input('Enter Number: ')
n = int(num)
print(factorial(n))