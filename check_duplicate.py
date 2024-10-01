def check_duplicate(nums):
    check = []
    for num in nums:
        if num in check:
            return True
        check.append(num)
    return False


arr = [1,2,3,3,4,4]
result =  check_duplicate(arr)
print(result)


arr = [1,2,3,5,6,7,8,9,4]
result =  check_duplicate(arr)
print(result)