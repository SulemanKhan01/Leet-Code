# ************ Brute Force ************ 

# def Search2D(arr , t):
#     for i in range(len(arr)):
#         arr2 = len(arr[i])
#         for j in range(arr2):
#             if arr[i][j] == t:
#                 return True
#     return False




# *************** Binary Search *************
def Search2D(arr , t):
    if not arr or not arr[0]:
        return False
    
    n = len(arr)
    m = len(arr[0])

    low = 0
    high = n*m - 1

    while low <= high:
        mid = (low + high)//2
        row = mid//m
        col = mid%m

        mid_val = arr[row][col]

        if mid_val == t:
            return True
        elif mid_val < t:
            low = mid + 1
        else:
            high = mid-1
    return False



matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
t = 6
print(Search2D(matrix , t ))


