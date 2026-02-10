def moveZeroes(nums):
    insert=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[insert] , nums[i] = nums[i] , nums[insert]
            insert+=1
print(moveZeroes(nums = [0,1,0,3,12]))