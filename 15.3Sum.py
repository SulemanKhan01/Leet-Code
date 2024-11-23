def threeSum(nums):
    result = []
    nums.sort()
    for i , t in enumerate(nums):

        if t > 0:
            break

        if i > 0 and t == nums[i-1]:
            continue

        l , r = i+1 , len(nums) - 1
        
        while l < r:

            threeSum = t + nums[l] + nums[r] 

            if threeSum > 0:
                r -= 1

            elif threeSum < 0:
                l += 1
                
            else:
                result.append([t , nums[l] , nums[r] ])
                l += 1
                r -=1

                while nums[l] == nums[l-1] and l<r :
                    l =+ 1
    return result
            

nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))

# Output: [[-1,-1,2],[-1,0,1]]

        