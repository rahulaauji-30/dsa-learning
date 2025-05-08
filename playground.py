def second_largest(nums):
    max_ele = 0
    second_lar = 0
    for num in nums:
        if max_ele < num:
            second_lar = max_ele
            max_ele = num
    print(second_lar)

second_largest([8, 8, 7, 6, 5])