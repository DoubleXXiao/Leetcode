# 153. 寻找旋转排序数组中的最小值
# 二分查找法
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while (low < high):
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]


'''
查找有序数组中的某个值，可以使用二分查找，原数组一定是有序的
时间复杂度为O(n),空间复杂度为O(1)
'''


def search_index(nums, target):
    low, high = 0, len(nums) - 1
    while (low <= high):
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
            pass
    return -1
    pass


'''
154. 寻找旋转排序数组中的最小值 II
考虑重复元素
'''


def findMin(nums):  # 考虑了重复元素的二分查找
    low, high = 0, len(nums) - 1
    while low < high:
        pivot = low + (high - low) // 2
        if nums[pivot] < nums[high]:
            high = pivot
        elif nums[pivot] > nums[high]:
            low = pivot + 1
        else:
            high -= 1
    return nums[low]


nums = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(search_index(nums, 7))
print(findMin(nums))

'''
263.简单
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。
'''


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        
        return n == 1