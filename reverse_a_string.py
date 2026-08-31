# reverse a string
class Solution:
    def rev_string(self, s: str) -> str:
        # Convert string to list for mutability
        chars = list(s)
        left, right = 0, len(chars) - 1
        swaps = 0

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            swaps += 1
            print("swap number", swaps)

        print("total swaps required are:", swaps)
        return ''.join(chars)



"""
left and right are two pointers
Left is 0 and right is len(s) -1 to reach last index value
"""
obj1 = Solution()
s = input("enter a string containing vowels")
print(obj1.rev_string(s))

"""
class Solution2:
        def reverseWords(self,s:str):  
            words = s.split()
            words = words[::-1]
            s = " ".join(words)
            print(s)                           
            return s
        
obj1=Solution2()      
x="what is my name"
obj1.reverseWords(x) 
"""