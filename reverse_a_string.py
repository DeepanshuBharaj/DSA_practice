# reverse a string
class solution():
    def rev_string(self,s:list[str]):
        i=1
        print(s,type(s))
        left,right= 0 , len(s) -1          # respectively 
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
            print("swap number ",i)
            i+=1
        
        print("total swaps required are :",i-1)     
        return s

"""
left and right are two pointers
Left is 0 and right is len(s) -1 to reach last index value
"""
obj1=solution()
s=list(input("enter a string containing vowels"))
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