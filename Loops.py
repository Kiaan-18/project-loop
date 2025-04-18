base=int(input("Enter the base number:"))
exponent=int(input("Enter the exponent: "))
print("The base is",base)
result=1
for i in range(exponent):
    result=result*base
print("The result of",base,"raised to the power of",exponent,"is",result )