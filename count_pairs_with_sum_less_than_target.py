from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort() 
        left = 0
        right = len(nums) - 1
        final_pairs = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                final_pairs += (right - left)
                left += 1
            else:
                right -= 1
        return final_pairs

# 1. Create a sample object of the Solution class
solution = Solution()

# 2. Define the first sample and target
nums1 = [-1, 1, 2, 3, 1]
target1 = 2

# 3. Define the second sample and target
nums2 = [-6, 2, 5, -2, -7, -1, 3]
target2 = -2

# 4. Run the code and print the results
result1 = solution.countPairs(nums1, target1)
print(f"Result 1: {result1}") # Expected output: 3

result2 = solution.countPairs(nums2, target2)
print(f"Result 2: {result2}") # Expected output: 10

#Complexity
# Time Complexity: O(n log n) :due to the sorting step. The two-pointer traversal only takes O(n) time, making this significantly faster than O(n^2) for larger arrays.
#Space Complexity: O(n) or O(1) depending on the sorting algorithm used under the hood (Python's built-in sort uses Timsort, which requires O(n) space).