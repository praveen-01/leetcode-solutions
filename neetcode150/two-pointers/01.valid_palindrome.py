class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<len(s) and s[i]==" ":
            i+=1
        while j>=0 and s[j]==" ":
            j-=1
        while i<=j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True