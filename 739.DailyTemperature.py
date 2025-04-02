def daily_temp(arr):

    n = len(arr)
    result = [0] * n

    for i in range(n):
        count = 0
        for j in range(i+1 , n):
            count += 1
            if arr[i] < arr[j]:
                
                result[i] = count
                break
        
    return result    





temperatures = [30,38,30,36,35,40,28]
print(daily_temp(temperatures))
