def twoSum(nums , target):
    hash_table = {}
    for i in range(len(nums)):
        goal = target - nums[i]
        if goal not in hash_table:
            hash_table[nums[i]] = i
        else:
            return [hash_table[goal],i]
        


arr = [3,4,5,6]
t = 7
print(twoSum(arr , t))


arr = [3,4,5,6,4,8]
t = 12
print(twoSum(arr , t))


arr = [3,5,6,10,9,19,0,3]
t = 7
print(twoSum(arr , t))