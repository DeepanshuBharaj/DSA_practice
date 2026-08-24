# LONGEST SUBSTRING WITHOUT REPLACEMENT
"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
# approach 1 : O(n2) TIMR LIMIT EXCEEDED
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        
        for i in range(len(s)):
            lst = []
            curr_count = 0
            
            # Start checking characters from index 'i' onwards
            for j in range(i, len(s)):
                if s[j] not in lst:
                    lst.append(s[j])
                    curr_count += 1
                    max_count = max(max_count, curr_count)
                else:
                    # As soon as we see a duplicate, this substring is done
                    break 
                    
        return max_count

sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))  


# SLIDING WINDOW n(O) for both
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using set to store only the unique elements
        char_set = set()
        left = 0  
        res = 0    # to store the max_length_of_substring

        for right in range(len(s)):
            # it works only when the duplicate value is found
            while s[right] in char_set:
                # remove the s[left] element from the char_set and left += 1 till the value s[right] is not already [present] in char_set
                char_set.remove(s[left])
                left += 1
            # else case runs every time
            char_set.add(s[right]) 
            res = max(res , (right - left) + 1)

        return res               

sol = Solution1()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))  