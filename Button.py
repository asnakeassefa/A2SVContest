from collections import defaultdict
 
total = int(input())
 
for _ in range(total):
    letters = defaultdict(list)
    string = input()
 
    for i,s in enumerate(string):
        letters[s].append(i)
    ans = []
    for key,value in letters.items():
        if len(value) % 2 != 0:
            ans.append(key)
        else:
            while len(value) > 0:
                if value.pop() - value.pop() != 1:
                    ans.append(key)
    ans=set(ans)
    ans = list(ans)
    ans.sort()
    res = ""
    for char in ans:
        res += char
    print(res)
