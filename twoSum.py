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
"""    
nums=[2,4,7,5]
target=12

solution=Solution()
result=solution.twoSum(nums,target)
print(result)
"""
# or python3
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # using hash_map
        hash_map = {}

        for i in range(len(nums)):
            # base case
            if i == 0:
                hash_map[nums[i]] = i
            else:
                reqd_val = target - nums[i]
                if reqd_val in hash_map:
                    return [hash_map[reqd_val], i]
                hash_map[nums[i]] = i

        return []


nums=[2,4,7,5]
target=12

solution=Solution2()
result=solution.twoSum(nums,target)
print(result)                    