def longest_consec(arr):
    main = []
    for i in range(len(arr)):
        subs = [arr[i]]
        for j in range(len(arr)):
            if arr[j] not in subs and arr[j]-arr[i] == 1:
                subs.append(arr[j])
        if len(subs) > 1:
            main.append(subs)
        else:
            pass
    

    count = len(main)

    return count 

nums = [2,20,4,10,3,4,5]

print(longest_consec(nums))