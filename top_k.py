def top_k_elements(nums , k):
    hash_table = {}
    for num in nums:
        if num in hash_table:
            hash_table[num] +=1
        else:
            hash_table[num] = 1

    sorted_dict = sorted(hash_table.items() , key=lambda item: item[1])
    sorted_dict.reverse()

    top_keys = sorted_dict[:k]

    final = []
    for key , value in top_keys:
        final.append(key)

    return final


        




nums = [1,2,2,2,2,2,2,2,3,3,4,5,5,5,5]
k = 3
print(top_k_elements(nums , k))
