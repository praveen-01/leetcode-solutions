#link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        else:
            c=0
            d1={}
            d2={}
            for i in range(len(s1)):
                if s1[i] not in d1:
                    d1[s1[i]]=1
                else:
                    d1[s1[i]]+=1
                if s2[i] not in d2:
                    d2[s2[i]]=1
                else:
                    d2[s2[i]]+=1
            for i in d1:
                if i not in d2 or d1[i]!=d2[i]:
                    return False
            for i in d2:
                if i not in d1 or d1[i]!=d2[i]:
                    return False
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    c+=1
                if c>2:
                    return False
            return c==0 or c==2
        
