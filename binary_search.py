"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity
"""

# approach 1 : brute force

class Solution1(object):
    def search(self, nums: list[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1
    
ob=Solution1()
nums = [1,2,9,63,64,78,90,273]
print(ob.search(nums,78))  

# Approach 2 : better {best}  O(log n)
class Solution(object):
    def search(self, nums: list[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        
        left , right = 0 ,len(nums) - 1   

        while left <= right:
            mid =left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1     

ob=Solution()
nums = [1,2,9,63,64,78,90,273]
print(ob.search(nums,273))               