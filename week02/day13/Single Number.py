def singlenumber(nums):
    result=0
    for num in nums:
        result^=num

    return result
print(singlenumber(nums = [4,1,2,1,2]))    