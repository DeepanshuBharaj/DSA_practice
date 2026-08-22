class Solution(object):
    def isPalindrome(self, x):
        original_x=x
        num_reversed=0
        last_digit=0
        while x>0:
         last_digit= x % 10
         num_reversed = num_reversed*10 + last_digit
         x = x // 10          
        if num_reversed==original_x:
            print("True")
        else:    
            print("False")

#creating an object of Solution class
obj1=Solution()

#calling the isPalindrome method
obj1.isPalindrome(121)