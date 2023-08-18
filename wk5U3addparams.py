"""Implement the function is_even(number) which gets an integer as input parameter 
and checks, if this input is even or not. is_even() will return the boolean value
True if the value is even and False if the input is not even.

Implement a for loop which iterates over the range(100).
 Within the for loop, the sequence-variable is checked with the function is_even().
 Depending on the return value, either x is even or x is not even is printed."""
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False     
for x in range(int(input("Enter number:"))):
    if is_even(x):
        print(x, "is even")
    else:
        print(x, "is not even")