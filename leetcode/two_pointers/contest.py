from collections import Counter

nums = [1,2,1]
k = 3
freq = Counter(nums)
print(freq.most_common()[0][1])

#print(Counter('abcdeabcdabcaba').most_common(2))
