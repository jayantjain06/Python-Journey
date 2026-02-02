def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            print("checking:",i,j)
            if nums[i]+nums[j]==target:
                return [i,j]
            
print(twoSum([1,2,3], 10))



        