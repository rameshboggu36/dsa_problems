# to get all the divisors we just need to check till the squareroot of N, 
# because the divisors will come in pairs, so if we check till sq N, we will get all divisors
N = 36

import math
checking_n = int(math.sqrt(N))
divisors = []
for i in range(1,checking_n+1):
    if N%i==0:
        if i==N//i:
            divisors.append(i)
        else:
            divisors.append(i)
            divisors.append(N//i)

print(divisors)