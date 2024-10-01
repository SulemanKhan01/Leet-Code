def Anagram(arr1 , arr2):
    l1 = sorted(arr1) 
    l2 = sorted(arr2)

    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

l1 = 'abcdefg'
l2 = 'gfedcba' 
result = Anagram(l1 , l2)
print(result)


l1 = 'abcd'
l2 = 'gfedcba' 
result = Anagram(l1 , l2)
print(result)