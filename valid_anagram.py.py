# valid Anagram "i.e. two strings havaing same letters but having different words order"
"""
time complexity is O(nlogn) which is due to sorted() which uses Timsort algorithm (a combination of merge sort and insertion sort)
space complexity is O(n) due to the space used by the sorted function
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
# So, the idea is to count the occurrences of each letter in one strings and decrease the count of values from the other string and check if the hash_map.values is == 0 
# O(n) for both tc and sc
class Solution2(object):
    def isAnagram(self, s, t):
        # base case
        if len(s) != len(t):
            return False

        # else case
        hash_map = {}  # frequency map
        # add value count of each value of s in a hash_map
        for val in s:
            if val in hash_map:
                hash_map[val] += 1
            else:
                hash_map[val] = 1

        # now the frquency map {hash_map} is prepared 
        for item in t:
            if item in hash_map:
                hash_map[item] -= 1
            else:
                return False  

        # check if count of each item in hash_map is 0 or not
        if all(val == 0 for val in hash_map.values()):
            return True
        return False
        """
        
sol2 = Solution2()
word1 = str(input("Enter string 1: "))
word2 = str(input("Enter string 2: "))
print(sol2.is_anagram(word1, word2))
#"""