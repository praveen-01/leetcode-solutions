class Solution:
    def findMin(self, nums: list[int]) -> int:
        i = 0
        j = len(nums)-1
        ans = float("inf")
        while i<=j:
            mid = (i+j)//2
            if nums[i]<=nums[mid]:
                ans = min(ans,nums[i])
                i = mid+1
            elif nums[mid]<=nums[j]:
                ans = min(ans,nums[mid])
                j = mid-1
        return ans
