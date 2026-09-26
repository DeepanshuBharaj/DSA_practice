class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum=0
        for i in range(len(nums)):
            running_sum += nums[i]
            nums[i] = running_sum
        return nums   

nums = [1,2,3,4,5,6,7,8,9,10] 
ob = Solution()
print(ob.runningSum(nums))       