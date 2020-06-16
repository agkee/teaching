# Two's complement

# Left shift, Right shift

# & | ^ (and, or, xor)
# xor: 0 ^ 0 = 0, 0 ^ 1 = 1, 1 ^ 1 = 0

# Get ith bit
# & with 1 << i and see if its 0 or 1
a = 8
if a & 1<<2: 
    print("It is true!")

# Set ith bit
# | with 1 << i
print(a)
a = a | 1<<2
a | 1<<2
print(a)

# Clear ith bit
a = a & ~(1<<2)
print(a)

a = 5 
b = 4 
print(a | b) 
print(a ^ b)