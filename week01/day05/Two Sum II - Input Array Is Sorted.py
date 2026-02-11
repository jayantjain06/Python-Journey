def twoSum(numbers, target):
    L=0
    R=len(numbers)-1
    
    while L<R:
        needed=numbers[L]+numbers[R]
        if needed>target:
            R -= 1
        elif needed<target:
            L += 1
        else:
            break
    return [L+1,R+1]
      
print(twoSum(numbers = [2,7,11,15], target = 9))