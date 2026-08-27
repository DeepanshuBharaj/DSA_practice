# move all the zeroes in an array to the end
class Solution:
    def moveZero(self, nums: list[int]) -> list[int]:
        next_non_zero = 0

        # using two pointer approach
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
                next_non_zero += 1

        return nums


ob = Solution()
nums = [1, 0, 342, 0, 4, 0, 346]
print(ob.moveZero(nums))        