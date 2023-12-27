
import math


def plus_one(nums):
    chars = ""
    array=[]
    for i in nums:
        chars += str(i)
    num = int(chars) + 1
    for j in str(num):
        array.append(int(j))
    return array

print(plus_one([1,2,3]))
