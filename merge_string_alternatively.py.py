# problem 1 = MERGE STRINGS ALTERNATIVELY
"""
eg. word1 ="abc" ,word2="xyz"
then return the merged string
"""
class Solution(object):
    def mergeAlternatively(self,word1,word2):
        i=0
        merged_string = []
        while (i <= len(word1)) or (i <= len(word2)):
            if i < len(word1):           # i != n {len(word1)}
                merged_string.append(word1[i])
            if i < len(word2):           # i!= m {len(word2)}
                merged_string.append(word2[i]) 

            # increement i
            i+=1  

        # Convert list into a single string
        result = "".join(merged_string)      
        return result         


sol=Solution()
print(sol.mergeAlternatively("Deepanshu","Bharaj"))

