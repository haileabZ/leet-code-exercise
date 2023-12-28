

def remove_duplicate(nums):
    for num in nums:
        if nums.count(num) > 1:
            nums.remove(num)
    return nums

print(remove_duplicate([1,2,2,2,3,3,4,5]))
