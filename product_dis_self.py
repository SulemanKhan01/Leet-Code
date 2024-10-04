def disclude_self(arr):
    final = []
    
    for i in range(len(arr)):
        result = 1
        for j in range(len(arr)):
            if j != i:
                result *= arr[j]
            else:
                pass
                
        final.append(result)
    return final

num = [1,2,3,4]

print(disclude_self(num))