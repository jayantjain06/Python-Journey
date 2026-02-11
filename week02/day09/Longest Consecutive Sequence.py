def longestConsecutive(nums):
    nums_set = set(nums)
    max_cons=0
    for num in nums_set:
        if num-1 not in nums_set:
            current=num
            current_cons=1
            while current+1 in nums_set:
                current+=1
                current_cons+=1
            max_cons=max(max_cons,current_cons)
    return max_cons        
print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))