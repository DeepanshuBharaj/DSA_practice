from typing import List

# Step 1: Define the class
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        v = [-1] * (n + 1)   # create an array of size n+1 filled with -1
        for num in nums:     # mark the numbers present
            v[num] = num
        for i in range(len(v)):  # find the missing one
            if v[i] == -1:
                return i
        return 0

# Step 2: Object creation
obj = Solution()

# Step 3: Function call with example input
nums = [3, 0, 1]   # Example input
result = obj.missingNumber(nums)

print("Missing number is:", result)
