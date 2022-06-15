

def thief(nums: list) -> int:
    house1, house2 = 0, 0
    for n in nums:
        temp = max(n + house1, house2)
        house1 = house2
        house2 = temp
    return house2

# nums = [1,3,1]
nums = [2, 5, 1, 3, 6, 2, 4]
# nums = [2, 10, 14, 8, 1]
print(thief(nums))
