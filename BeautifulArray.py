Total = int(input())
 
set1 = set()
set1Count = 0
set2 = set()
set2Count = 0
set3 = set()
set3Count = 0
 
nums = list(map(int,input().split()))
negativeNums = 0
negativeCount  = 0
posetive = 0
for num in nums:
	if num < 0:
		negativeNums += 1
	elif num > 0:
		posetive += 1
for num in nums:
	if num < 0:
		if negativeCount == 0:
			set1.add(num)
			negativeCount += 1
			set1Count += 1
		elif posetive == 0 and negativeCount < 3:
			set2.add(num)
			negativeCount += 1
			set2Count += 1
		elif negativeCount > 0 and negativeNums % 2 == 0:
			set3.add(num)
			set3Count += 1
		elif negativeCount > 0 and negativeNums % 2 != 0:
			set2.add(num)
			set2Count += 1
	elif num == 0:
		set3.add(num)
		set3Count += 1
	elif num > 0:
		set2.add(num)
		set2Count += 1
	
print(set1Count, end = " ")
print(*set1)	
print(set2Count, end = " ")
print(*set2)
print(set3Count, end = " ")
print(*set3)
