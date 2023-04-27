
import math

num = int(input())

newNum = math.floor(math.sqrt(num))

while newNum > 1:
    if not num % newNum and math.gcd(newNum,num//newNum) == 1:
        break
    newNum -= 1
    
print(newNum,num // newNum)