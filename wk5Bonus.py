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