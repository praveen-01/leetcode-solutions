class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        while i<=j:
            cur_sum = nums[i]+nums[j]
            if cur_sum==target:
                return [i+1,j+1]
            elif cur_sum>target:
                j-=1
            else:
                i+=1
        return [-1,-1]