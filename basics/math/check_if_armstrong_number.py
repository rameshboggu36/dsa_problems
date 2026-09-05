# Armstrong number is when we raise the power of each digit to number of digits 
# in the number and add them, it will give the original number. 

import math
N = 9474
tem_N = N
sum_n = 0 

digits = int(math.log10(N))+1
while N>0:
    sum_n = sum_n + int(math.pow(N%10,digits))
    N = N//10

print(sum_n==tem_N)
