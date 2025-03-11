def buy_sell_stock(nums):

    minx = min(nums)

    mini = nums.index(minx)

    nums2 = nums[mini:]

    max2 = max(nums2)

    profit = max2 - minx

    return(profit)

prices = [10,1,5,6,7,1]

print(buy_sell_stock(prices))
