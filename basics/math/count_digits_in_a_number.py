N = 123459098765456789
# Brute force approach: Time complexity is O(logN)
count = 0
while N>0:
    count +=1
    N = N//10
print(count)

# Optimal approach: Time complexity O(1)
# Because the value of log10(100) is 2 and log10(1000) is 3 
# so the numbers between 100 and 1000 will have value between 2 and 3
# so we take the floor of the value from the log10 of the value and 1 to it to match the correct count of digits. 
# we are adding 1 because, for example for 1000 the log will be 3 but the digits are 4, for that we are adding 1
# another example, for 899 the log10 value is 2.95 so it will be 2+1 which is 3 
import math
N = 123459098765456789
digits = int(math.log10(N))+1
print(digits)