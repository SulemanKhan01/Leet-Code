def twoSum(numbers , target):
    hash = {}
    indice = 0
    for num in numbers :
        indice +=1
        goal = target - num

        if goal not in hash:
            hash[num] = indice

        else:
            print(hash)
            return [hash[goal] , indice]

    # OR
    # for indice , num in enumerate(numbers , start=1):
    #     hash[indice] = num


numbers = [3,4,5,6,4,8]

print(twoSum(numbers , 12))