def twoSum (nums,target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i

print (twoSum(target = 6, nums = [3,3]))