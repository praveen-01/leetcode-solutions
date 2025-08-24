class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        org = [0]*26
        for i in s1:
            org[ord(i)-ord('a')]+=1
        i = 0
        org2 = [0]*26
        for j in range(len(s2)):
            if j-i+1<len(s1):
                org2[ord(s2[j])-ord('a')]+=1
            else:
                org2[ord(s2[j])-ord('a')]+=1
                if org==org2:
                    return True
                org2[ord(s2[i])-ord('a')]-=1
                i+=1
        return False
