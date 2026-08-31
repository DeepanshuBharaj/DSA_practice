#Qn. Given a sorted array of distinct integers and a target value,return the index if the target is found. if not return the index where it would be if it were inserted in order
# hint(for self) : use binary search as it is required to be done in O(nlogn ) time-complexity
class Solution:
    def searchInsert(self,nums:list[int],target:int)->int:
        left=0
        right=len(nums)-1

        while left<=right:
            mid= (left + right) // 2

            if nums[mid] == target:
                return mid
                
            elif nums[mid] >target:
                right=mid-1
            else:
                left=mid+1

        return left

object=Solution()
nums=[13,14,17,19,30]
target=99          
print(object.searchInsert(nums,target))     