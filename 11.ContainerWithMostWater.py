def maxArea(heights):
    result = 0
    l , r = 0 , len(heights)-1

    while l < r:
        area = (r-1) * min(heights[l] , heights[r])
        result = max(result , area)

        if heights[l] < heights[r]:
            l +=1
        else:
            r -=1
    return result

height = [1,7,2,5,4,7,3,6]
print(maxArea(height))






        