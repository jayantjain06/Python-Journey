def maxArea(height):
    n=len(height)
    max_amount=0
    
    for L in range(n):
        for R in range(L+1,n):
            amount = min(height[L], height[R]) * (R - L)
            max_amount = max(amount, max_amount)       
    return max_amount    
print(maxArea(height =[1,8,6,2,5,4,8,3,7]))