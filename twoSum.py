#time complexity : O(n)
#space complexity : O(n) as in the worst case we might have to store each number in the dictionary
class Solution:
    def twoSum(self,nums,target): 
        hash_table={}                    #using hash_map to store nums and improve the complexity of the program
        for i , num in enumerate(nums):
            complement=target-num
            if complement in hash_table:
                return [hash_table[complement],i]
            hash_table[num] = i          
        return [] 
    
nums=[2,4,7,5]
target=12

solution=Solution()
result=solution.twoSum(nums,target)
print(result)