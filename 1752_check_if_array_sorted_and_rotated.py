# for a array to be sorted and rotated we should only have one index with its next value lesser
#count the no.of index where the above condition is true
#if count greter than 1 then return False
# else true
#link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        res=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                res+=1
        return True if res<=1 else False         
        
