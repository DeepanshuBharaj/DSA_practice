"""
class Solution(object):
    def removeElement(self, nums, val):
        
        n=0
        list=[]
        for i in range(0,len(nums)):
            if nums[i] == val:
                continue
            else:
                list.append(nums[i])   
        return len(list),list  
ob=Solution()
nums=[1,2,7,7,4,7,4,7]
print(ob.removeElement(nums,7))  
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # moving valid element forward
                k+=1
        return k

obj1=Solution()
nums=[1,2,2,2,3,4,5,1,2,3]
print(obj1.removeElement(nums,2))   
