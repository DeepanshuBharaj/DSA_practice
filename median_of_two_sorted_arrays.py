class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # merge arrays
        new_array = []
        i=0
        while i<len(nums1) or i<len(nums2):
            if i<len(nums1):
                new_array.append(nums1[i])
            if i<len(nums2):
                new_array.append(nums2[i])

            i += 1
        # return median
        new_array.sort()
        # for odd count we have a direct median
        if len(new_array)%2 != 0:
            return new_array[len(new_array)//2]
        else :
            return (new_array[len(new_array)//2 -1] + new_array[(len(new_array)//2)]) / 2  

nums1 = [1,2,3]
nums2 = [6,7,8,9,0]

ob1 = Solution()

print(ob1.findMedianSortedArrays(nums1,nums2))