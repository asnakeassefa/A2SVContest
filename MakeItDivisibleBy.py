from collections import defaultdict

total = int(input())

for _ in range(total):
    nums = input()
    main = defaultdict(int)
    length = len(nums)
    ans = 0
    for i in range(length-1,-1,-1):
        if not main["5"] and nums[i] == "5":
            main["5"] = i
        elif main["5"] and (nums[i] == "7" or nums[i] =="2"):
            ans = length-2 - i
            break
            
        if not main["0"] and nums[i] == "0":
            main["0"] = i
        elif main["0"] and (nums[i] == "0" or nums[i] == "5"):
            ans = length-2 - i
            break
    print(ans)