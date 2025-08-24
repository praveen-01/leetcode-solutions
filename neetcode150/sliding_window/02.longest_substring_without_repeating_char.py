'''
to-do: try without inner loop, we can store the idx of each character as we pass and if we see an char already in d then max len would be current-idx of that char
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        d = {}
        for j in range(len(s)):
            if s[j] in d:
                while s[j] in d:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    i+=1
            d[s[j]]=1
            ans=max(ans,len(d))

        return ans
        