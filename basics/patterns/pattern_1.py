# Print a pattern(*):
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
rows = 5
columns = 5
for i in range(rows):
    for j in range(columns):
        print("*",end=" ")
    print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print()



# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
for i in range(rows):
    for j in range(i+1):
        print(i+1,end=" ")
    print()



# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
for i in range(rows):
    for j in range(columns-i):
        print("*",end=" ")
    print()


# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
for i in range(rows):
    for j in range(columns-i):
        print(j+1,end=" ")
    print()


#         *       
#       * * *     
#     * * * * *   
#   * * * * * * * 
# * * * * * * * * * 
for i in range(rows):
    for j in range(2 * rows - 1):
        if rows - i - 1 <= j <= rows + i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# * * * * * * * * * 
#   * * * * * * *   
#     * * * * *     
#       * * *       
#         *  
for i in range(rows-1,-1,-1):
    for j in range(2 * rows - 1):
        if rows - i - 1 <= j <= rows + i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#         *         
#       * * *       
#     * * * * *     
#   * * * * * * *   
# * * * * * * * * * 
# * * * * * * * * * 
#   * * * * * * *   
#     * * * * *     
#       * * *       
#         *  
for i in range(rows):
    for j in range(2 * rows - 1):
        if rows - i - 1 <= j <= rows + i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(rows-2,-1,-1):
    for j in range(2 * rows - 1):
        if rows - i - 1 <= j <= rows + i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

for i in range(2*rows-1):
    if i>=rows:
        for j in range(2*rows-i-1):
            print("*", end=" ")
    else:
        for j in range(i+1):
            print("*", end=" ")
    print()



# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 
for i in range(rows):
    for j in range(i+1):
        if (i+j)%2==0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()



# 1             1 
# 1 2         2 1 
# 1 2 3     3 2 1 
# 1 2 3 4 4 3 2 1 
for i in range(rows-1):
    for j in range(i+1):
        print(j+1,end=" ")
    for j in range(i+1,2*rows-3-i):
        print(" ",end=" ")
    for j in range(2*rows-2-i,2*rows-1):
        print(2*rows-j-1,end=" ")
    print()

# alternate and better approach
for i in range(rows - 1):
    # Left side
    for j in range(i + 1):
        print(j + 1, end=" ")

    # Middle spaces
    for j in range(2 * (rows - i - 2)):
        print(" ", end=" ")

    # Right side
    for j in range(i + 1):
        print(i - j + 1, end=" ")

    print()

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
counter = 1
for i in range(rows):
    for j in range(i+1):
        print(counter, end=" ")
        counter+=1
    print()

# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
for i in range(rows):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()


# A B C D E 
# A B C D 
# A B C 
# A B 
# A 
for i in range(rows):
    for j in range(rows-i):
        print(chr(65+j), end=" ")
    print()


# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
for i in range(rows):
    for j in range(i+1):
        print(chr(65+i), end=" ")
    print()


#       3       
#     2 3 4     
#   1 2 3 4 5   
# 0 1 2 3 4 5 6 
n=4
for i in range(n):
    for j in range(2*n-1):
        if n-i-1 <= j <= n+i-1:
            print(chr(64+i + 1 - abs(n - 1 - j)), end=" ")
        else:
            print(" ", end=" ")
    print()