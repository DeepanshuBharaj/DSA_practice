# contains Duplicates :-
"""
if the given integer array contains any duplicate items retrun True else return False
"""

"""
# Approach1
class Solution1:
    def contains_duplicates(self,nums: list[int])->bool:

        for i in range (0,len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

sol=Solution1()
array=[11,23,21,2,24,24] 
print(sol.contains_duplicates(array))           
"""
# approach2  "by sorting first and then just comparing the next number with the current one "
"""
it is a better approach with a time complexity of O(nlogn)

"""
"""
class Solution2:
    def contains_duplicates(self,nums:list[int])->bool:
        nums.sort()

        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
sol2=Solution2()
array=[11,23,21,2,24,24] 
print(sol2.contains_duplicates(array))           
"""

# approach3 "using set (as it doesnot contain duplicates)"
"""
class Solution3:
    def contains_duplicates(self,nums:list[int])->bool: 
        return True if len(set(nums)) < len(nums) else False 
    
sol3=Solution3()
array=[11,23,21,21,24] 
print(sol3.contains_duplicates(array))     
"""

# approach3 "we use set(empty one) . every time we find a number we will check set. and if the same number is present in set , we return True"

class Solution4:
    def contains_duplicates(self,nums:list[int])->bool:
        num_set=set()   # empty set

        for i in nums:
            if i in num_set:
                return True 
            else:
                num_set.add(i)
        return False    
    
sol4=Solution4()
array=[11,23,21,21,24] 
print(sol4.contains_duplicates(array))  
