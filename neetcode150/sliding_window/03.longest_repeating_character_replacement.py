class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        d = {}
        ans = 0
        for j in range(len(s)):
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            while (j-i+1)-max(d.values())>k:
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1
            ans = max(ans,j-i+1)
        return ans
