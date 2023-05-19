import heapq

num = input()
ans = input()

newNum = []
count = ""
for n in num:
    if n == "0":
        count += "0"
    else:
        newNum.append(n)
newNum.sort()
if newNum:
    newNum[0] += count
    result = "".join(newNum)
else:
    result = count
# print(newNum)
if result == ans:
    print("OK")
else:
    print('WRONG_ANSWER')