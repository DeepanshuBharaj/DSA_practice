# given a sorted non decreasing array/list nums
# finding two nums which sum up to give the target value
# have to solve in O(1) space complexity

# time-complexity=O(n)
# space-complexity=O(1) 

class solution:
    def two_sum(self,nums:list,target):
        l=0
        r=len(nums)-1
        while l<r:
            total = nums[l]+nums[r]
            if total == target:
                print(l+1,r+1)
                return [l+1,r+1]
            elif target > total:
                l +=1
            elif target < total:
                r -=1  
        return [-1,-1]
                
obj=solution()
nums=[1,2,4,5]
print(obj.two_sum(nums,6) )           