def rotate(nums , k):
    
    if len(nums) == 0:
        return nums
    
    final = []
    for i in range(k):
        final.append(nums[-1])
        nums.pop()

    return final[::-1]

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums , k))



        
        