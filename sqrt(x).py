"""
short-cut method :-

sqrt = x ** 0.5
result=int(sqrt)
print(result)
"""


# best approach - using binary search t(c)=O(log x)
class Solution(object):
    def mySqrt(self, x):
        #base case
        if x == 0 or x == 1:
            return x

        left,right=0 , x//2          # x//2 is better while having a large number

        # iterating while loop till left is smaller than or equal to right
        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            
            elif mid * mid < x:
                left = mid + 1

            else:
                right = mid - 1

        # return right if loop breaks        
        return right
""""""


# brute force
class solution2:
    def sqrt2(self,x:int)->int:
        # base cases
        if x==0 or x==1: 
            return x
        
        i=1
        
        while (i*i <= x ):
            i+=1
        
        #when while loop breaks
        return i-1
       
            
""""""      
            
         
            
obj=Solution()
obj2=solution2()
print(obj.mySqrt(9))       # best apprach wala         
#print(obj2.sqrt2(4))