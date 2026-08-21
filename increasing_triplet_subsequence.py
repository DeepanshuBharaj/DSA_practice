# it is only for checking consecutive occurences not non_censcutive ones

class Solution:
    def find_Triplet(self,nums):

        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] < nums[i+2]:
               print("True , triplet exists")
              # print(i)           
               return True
            
        print("False , triplet doesnot exists")
        return False   
        

"""         
ob1=Solution()
nums=[1,2,-3,-44,2342,12333,1222222]     
ob1.find_Triplet(nums)
"""
# to check non_consective subsequences TC: O(n) and SC: O(1)
class Solution2:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf') 

        for i in range(len(nums)):
            # for the smalles one 
            if nums[i] <= min1:
                min1 = nums[i]     # update 1st minimum

            # loop reaches here only if nums[i] > min1  
            elif nums[i] <= min2:
                min2 = nums[i]     # update 2nd minimum

            # {loop reaches here strictly if nums[i] > min2 > min1} 
            else:
                return True       # Found a third number greater than both
            
        return False   # No triplet found 
        
        
    
ob1=Solution2()
nums=[2,1,5,0,4,6]        # true :One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
print(ob1.increasingTriplet(nums))   

"""
The "Tricky" Edge Case (Historical Markers)
The most confusing part of this algorithm is when min1 updates after min2 is already set.

Imagine the array [5, 6, 1, 7]:

num = 5: min1 becomes 5.

num = 6: min2 becomes 6. (We have a valid pair: 5, 6).

num = 1: min1 updates to 1. min2 remains 6.

num = 7: 7 is greater than min1 (1) and min2 (6). Returns True.

Notice that when the algorithm returns True, min1 is 1 and min2 is 6, which appear out of order in the original array.
This works perfectly anyway because the existence of min2 = 6 acts as a historical marker.
It proves that at some point in the past, there was a number smaller than 6 (which was the 5).
We don't need min1 to explicitly hold that 5 anymore;
 we just need to know we can safely append the 7 to complete the triplet (5, 6, 7)"""

# if we need to return the values also then 
class Solution3:
    def increasingTripletValues(self, nums: list[int]) -> list[int] | list:
        min1 = float('inf')
        min2 = float('inf')
        
        # This will lock in the valid first number of our pair
        seq_min1 = float('inf') 
        
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
                # We found a valid second number! 
                # Lock in the current min1 as the official start of this pair.
                seq_min1 = min1 
            else:
                # We found the third number! 
                # Return the locked-in first number, the second number, and the current number.
                return [seq_min1, min2, num] 
                
        return [] # Return an empty list if no triplet exists

    
ob1=Solution3()
nums=[2,1,5,0,4,6]        
print(ob1.increasingTripletValues(nums))     