class solution():
    def merge_strings(self,word1,word2):
        rstring=[]
        i=0
        while i<len(word1) or i<len(word2):
            if i<len(word1):
             rstring.append(word1[i])
            if i<len(word2):
                rstring.append(word2[i])
            i+=1
        print("following is the resultant string")
        print(''.join(rstring))
        return ''.join(rstring)           #join keyword is used to join the string value aquired along with ''. to join it in a word
obj1=solution() 

x=str(input("enter word1 :"))
y=str(input("enter word2 :"))

obj1.merge_strings(x,y) 
