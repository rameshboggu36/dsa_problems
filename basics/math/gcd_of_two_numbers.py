# this is euclid's method for computing GCD
# we have to divide the maximum number with minimum number until min becomes 0
# after each division, we modify the max with min and min with remainder

# Another approach is to find all divisors of both numbers
# and find the greatest common divisor among them.

n=25
m=150

min_nm = min(n,m)
max_nm = max(n,m)

while min_nm>0:
    max_nm, min_nm = min_nm, max_nm % min_nm

print(max_nm)
