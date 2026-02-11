def maxArea(height):
    max_area=0
    L=0
    R=len(height)-1
    while L<R:
        area = min(height[L],height[R])*(R-L)
        max_area=max(area,max_area)
        if height[L]<height[R]:
            L+=1
        else:
            R-=1
    return max_area

print(maxArea(height = [1,8,6,2,5,4,8,3,7]))