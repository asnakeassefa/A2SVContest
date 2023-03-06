from collections import defaultdict
 
total = int(input())
namedict =defaultdict(int)
names = list(input().split(" "))
newTotal = int(input())
newcome = [input() for i in range(newTotal)]
 
for name in newcome:
    namedict[name] = -1
newcome.sort()
count = 0
breaking = False
for i,name in enumerate(names):
    while name > newcome[count]:
        namedict[newcome[count]] = i
        count += 1
        if newTotal == count:
            breaking = True
            break
    if breaking:
        break
for val in namedict.values():
    if val == -1:
        print(total)
    else:
        print(val)
