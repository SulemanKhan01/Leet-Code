def rotate(nums , k):
    
    if len(nums) == 0:
        return nums
    
    final = []
    for i in range(k):
        final.append(nums[-1])
        nums.pop()
    new_final = final[::-1]
    for num in nums:
        if num in new_final:
            return new_final
        new_final.append(num)

    return new_final

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums , k))



        
        