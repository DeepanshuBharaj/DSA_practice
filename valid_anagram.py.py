# valid Anagram "i.e. two strings havaing same letters but having different words order"
"""
this approach is using sorting to check if two strings are anagrams
time complexity is O(nlogn) which is due to sorted() which uses Timsort algorithm (a combination of merge sort and insertion sort)
space complexity is O(n) due to the space used by the sorted function

"O(n) > O(nlogn) as O(n) is linear and O(nlogn) is logarithmic i.e. O(nlogn) contains logn which states that time increases logarithmically with the input size"
"""
"""
class Solution:
    def is_anagram(self , s: str , t: str )->bool:
        if len(s) == len(t):
            #return True
            if sorted(s) == sorted(t):
                return True
            else:
                return False
        else:
            return False

sol=Solution()
word1=str(input("enter string 1"))
word2=str(input("enter string 2"))
print(sol.is_anagram(word1,word2)) 
"""
#"""
# APPROACH 2 " using a dictionary to count occurrences of each character"
# Anagrams are words that contain the same characters in different orders. 
# So, the idea is to count the occurrences of each letter in both strings and compare them
# O(n) for both tc and sc
class Solution2:
    def is_anagram(self , s: str , t: str )->bool:

        # If the lengths of the strings are not equal, they cannot be anagrams      
        if len(s) != len(t):
            return False
        
        # Create a dictionary to count occurrences of each character
        dictionary = {}


        # Count occurrences of each character in the first string
        for value in s:
            if value in dictionary:
                dictionary[value] += 1
            else:
                dictionary[value] = 1


        # Decrease the count for each character in the second string
        for value in t:
            if value in dictionary:
                dictionary[value] -=1
            elif value not in dictionary or dictionary[value] < 0:
                return False
            
        
        # If all values in the dictionary are zero, then the strings are anagrams
        if all(value == 0 for value in dictionary.values()):
            return True
        else:
            return False
        
        """ or for above last code
        return not any(dictionary.values()) 
        # This works because if any value is non-zero, any(dictionary.values()) will be True, and the not flips it

        #or
        return sum(dictionary.values()) == 0      # it will return bool value

        """
        
sol2 = Solution2()
word1 = str(input("Enter string 1: "))
word2 = str(input("Enter string 2: "))
print(sol2.is_anagram(word1, word2))
#"""