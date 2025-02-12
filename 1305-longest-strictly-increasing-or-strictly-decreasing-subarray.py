# check for increasing subarray and descresing subarray seperately
# link: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=1
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[j]<=nums[j-1]:
                    break
                j+=1
            ans=max(ans,j-i)
            i=j
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[j]>=nums[j-1]:
                    break
                j+=1
            ans=max(ans,j-i)
            i=j
        return ans
        
