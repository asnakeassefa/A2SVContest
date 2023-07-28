total = int(input())

for _ in range(total):
    num = int(input())
    i = 9
    ans = []
    while num:
        if num - i > -1:
            num -= i
            ans += str(i)
        i -= 1
    ans.sort()
    res = ""
    for val in ans:
        res += val
    print(res)