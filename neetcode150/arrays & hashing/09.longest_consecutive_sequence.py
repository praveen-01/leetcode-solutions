class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        maxi = 0
        for i in freq:
            if i-1 in freq: continue
            else:
                count = 1
                while i+1 in freq:
                    count+=1
                    i+=1
                maxi = max(maxi,count)
        return maxi