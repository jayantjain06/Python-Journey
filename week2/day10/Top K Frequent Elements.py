import heapq
def topKfrequent(nums ,k):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num]=0
        freq[num] += 1
    return heapq.nlargest(k, freq.keys(), key=freq.get)
    

print(topKfrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))
