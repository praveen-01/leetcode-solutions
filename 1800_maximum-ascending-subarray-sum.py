#link: https://leetcode.com/problems/maximum-ascending-subarray-sum
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi=max(nums)
        n=len(nums)
        i=0
        while i<n:
            j=i+1
            temp=nums[i]
            while j<n:
                if nums[j]<=nums[j-1]:
                    break
                temp+=nums[j]
                j+=1
            maxi=max(maxi,temp)
            i=j
        return maxi
        
