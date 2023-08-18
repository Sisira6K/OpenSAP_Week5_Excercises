"""Prime numbers are natural numbers greater than 1 which are not divisible by any number beside 1
and the number itself. In other words, the number cannot be composed as a product of two natural 
numbers other than 1 and the number itself. There are infinite prime numbers and the first ones are:

2, 3, 5, 7, 11, …
Write a program, that gets an integer through input and creates a list containing all prime numbers
until this input. To do so, two functions have to be implemented:

The function is_prime() gets an integer as input and returns True if this integer is prime,
and False if the integer is not prime.
The function prime_list() gets an integer as input and checks each number from 2 to input, 
if it is prime by calling the above function. If a number is prime, it is appended to a list. 
This list is given back as the return value of prime_list().
The program finally outputs the list of all prime numbers.

Example 1:

Up to which number do you want all prime numbers: 100
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def prime_list(number):
    prime_numbers = []
    for x in range(2, number):
        if  is_prime(x):
            prime_numbers.append(x)
    return prime_numbers

x = int(input("Up to which number do you want all prime numbers: "))
print(prime_list(x))