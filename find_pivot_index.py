# if any find pivot index ( where the sum of numbers in the left is equal to the numbers in the right)
class solution:
    def find_pivot(self,nums:list[int]) -> int :

        total=sum(nums)   #O(n)

        leftSum=0

        for i in range(len(nums)):
            rightSum=total - nums[i] - leftSum    # logic
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1     

ob1 = solution()
nums=[0,2,3,-4,6]
print(ob1.find_pivot(nums))