# each fibonacci number is the sum of the two preceding ones
class Solution:
    def fib_number(self,n:int)->int:
        a, b = 0, 1

        for _ in range(n):
            a,b = b, a+b
        return a

    def fibonacci_sequence(self,n:int)->list[int]:
        a, b = 0, 1
        sequence = []
        for _ in range(n):
            sequence.append(a) # value
            a, b = b, a + b    # move forward
        return sequence


    
        
ob1=Solution()
num=4
print(ob1.fib_number(num))   
print(ob1.fibonacci_sequence(10))  

""" FOR FIB_NUMBER
Time Complexity: O(n)
Space Complexity: O(1) 

FOR FIB_AEQUENCE
Time Complexity: O(n)
Space Complexity: O(n) [as a list is to be used to save n numbers]  

"""

# [0 , 1 , 1 , 2 , 3 , 5 , 8 , 13]

