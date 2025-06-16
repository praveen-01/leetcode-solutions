class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        greatest_max = []
        for i in nums[::-1]:
            if not greatest_max:
                greatest_max.append(i)
            else:
                greatest_max.append(max(greatest_max[-1],i))
        greatest_max = greatest_max[::-1]
        res = -1
        for i in range(1,len(nums)):
            if greatest_max[i]>nums[i-1]:
                res=max(res,greatest_max[i]-nums[i-1])
        return res

        
