def missingNumber(nums):
    n = len(nums)
    cur_sum=sum(nums)
    exp_sum=n*(n+1)//2
    return exp_sum-cur_sum


print(missingNumber(nums = [9,6,4,2,3,5,7,0,1]))