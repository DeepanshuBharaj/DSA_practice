# Q.977.squares of a sorted array
class solution:
    def sorted_squares(self,nums: list[int]):
        print("numbers in the given list are : ",nums)
        for i in range(len(nums)):
           nums[i]=nums[i]**2
        return sorted(nums)           #here the sorted keyword is used to sort the elemts in the list in the ascending order

obj1=solution()
nums=[1,-6,-2,3,-4,5]
print(obj1.sorted_squares(nums))