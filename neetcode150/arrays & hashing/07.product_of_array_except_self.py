class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in nums:
            if not prefix:
                prefix.append(i)
            else:
                prefix.append(i*prefix[-1])
        
        suffix = []
        for i in nums[::-1]:
            if not suffix:
                suffix.append(i)
            else:
                suffix.append(i*suffix[-1])
        suffix = suffix[::-1]
        res = []
        res.append(suffix[1])
        for i in range(len(nums)-2):
            res.append(prefix[i]*suffix[i+2])
        res.append(prefix[-2])
        return res 
        