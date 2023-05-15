import heapq

total = int(input())

for _ in range(total):
    n,m = map(int,input().split())
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))

    heapq.heapify(nums1)

    for num in nums2:
            heapq.heappop(nums1)
            heapq.heappush(nums1,num)
    print(sum(nums1))