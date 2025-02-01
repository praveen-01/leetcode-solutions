#link https://leetcode.com/problems/special-array-i/description
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        else:
            start = 1 if nums[0]%2!=0 else 0
            for i in range(0,len(nums),2):
                if nums[i]%2!=start:
                    return False
            for i in range(1,len(nums),2):
                if nums[i]%2==start:
                    return False
            return True

        
