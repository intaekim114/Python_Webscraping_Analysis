
def is_prime(x): 
    for i in range(2, x):
    	if x % i == 0:
        	return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    print(primes)

find_primes(1, 10)