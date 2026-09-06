# to check a number is prime, we need to check the divisors, 
# if there are other divisors than 1 and the number itself, 
# then it is not a prime
N = 391

import math
checking_n = int(math.sqrt(N))
prime = True
for i in range(1,checking_n+1):
    if N%i==0:
        if i!= 1 and i!=N:
            prime = False
            break
print(prime)