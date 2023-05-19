from collections import defaultdict, deque


total = int(input())

def compLetter(word1,word2,graph,indeg,res):
    length1 = len(word1)
    length2 = len(word2)
    MinLength = min(length1,length2)

 ###abc bc
    for i in range(MinLength):
        if word1[i] != word2[i]:
            indeg[word2[i]] += 1
            graph[word1[i]].append(word2[i])
            break
    else:
        if length1 > length2:
            res[0] = True

words = []
for _ in range(total):
    words.append(input())
graph = defaultdict(list)
indeg = defaultdict(int)
res = [False]
for i in range(total-1):
    compLetter(words[i],words[i+1],graph,indeg,res)
    if res[0]:
        break

queue = deque()

if not res[0]:
    for i in range(ord('a'), ord('a') + 26):
        if indeg[chr(i)] == 0:
            queue.append(chr(i))

ans = []
while queue:
    node = queue.popleft()
    ans.append(node)
    for value in graph[node]:
        indeg[value] -= 1
        if indeg[value] == 0:
            queue.append(value)

if len(ans) != 26 or res[0]:
    print("Impossible")
else:
    print("".join(ans))