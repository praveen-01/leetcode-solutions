class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        for i in range(len(nums)):
            target_to_look = target-nums[i]
            if target_to_look in freq_map:
                return [freq_map[target_to_look],i]
            freq_map[nums[i]] = i
        return [-1,-1]
        