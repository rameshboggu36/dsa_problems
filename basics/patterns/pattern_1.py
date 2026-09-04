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