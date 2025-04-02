def multiply_arrays(arr1, arr2):
    # Result array size will be at most len(arr1) + len(arr2)
    result = [0] * (len(arr1) + len(arr2))

    # Multiply each digit of arr1 with each digit of arr2
    for i in range(len(arr1) - 1, -1, -1):
        for j in range(len(arr2) - 1, -1, -1):
            mul = arr1[i] * arr2[j]
            pos1 = i + j
            pos2 = i + j + 1

            # Add multiplication result to result array
            sum_ = mul + result[pos2]
            result[pos2] = sum_ % 10  # Store last digit
            result[pos1] += sum_ // 10  # Carry to next position

    # Remove leading zeros
    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    return result


# Example Usage:
arr1 = [1, 2, 3 , 4]  # Represents 123
arr2 = [1, 2 ,3 , 4]     # Represents 45

result = multiply_arrays(arr1, arr2)
print(result)  # Output: [5, 5, 3, 5] (123 * 45 = 5535)
