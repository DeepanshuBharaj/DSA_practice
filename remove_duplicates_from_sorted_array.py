# Qn. Given an integer array nums sorted in non-decreasing order , remove the duplicates in-place such that relative order of the elements should be kept same . Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things.



# method 1 with time complexity = O(n^2) due to the 'in' operator used in if condtition and space complexity =O(n)
class solution:
    def removeDuplicates(self,nums:list[int])->list:
        list_without_duplicates=[]
        for x in nums:
            if x not in list_without_duplicates:
                list_without_duplicates.append(x)
        return list_without_duplicates

# method 2 optimized version for time complexity O(n) and space complexity O(n)
class Solution:
    def remove_duplicates(self,nums:list[int])->list:
        #using set because set lookups ans insertions take O(1) on avg.
        num_set=set()
        list_without_duplicates=[]
        for x in nums:
            if x not in num_set:
                list_without_duplicates.append(x)
                
                #also add it in num_set
                num_set.add(x)
        return list_without_duplicates        
                   
# method 3 using a dict insertion order to remove duplicates while preserving order.
class solution3:
    def remove_duplicates(self,nums:list[int])->list:
        return list(dict.fromkeys(nums))   # method dict.fromkeys creates a dictionary wtih elements of nums as keys,automatically removing duplicates while preserving the order
    # the resultant dictionary is converted back to the list


# new_lst = set(nums)  : TC AND SC = O(n) as insertion into set takes O(n) 

object=Solution()
object1=solution()
object2=solution3()
nums=[15,15,15,23,56,79,79,79,80]   
print(object2.remove_duplicates(nums))     