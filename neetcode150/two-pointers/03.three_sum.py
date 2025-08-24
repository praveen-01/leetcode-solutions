class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        i = 0
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            #target = -nums[i]
            #d = {}
            j = i+1
            k = len(nums)-1
            while j<k:
                cur_sum = nums[i]+nums[j]+nums[k]
                if cur_sum==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    while j<k and nums[j+1]==nums[j]:
                        j+=1
                    while k>j and nums[k-1]==nums[k]:
                        k-=1
                    j+=1
                    k-=1
                elif cur_sum>0:
                    k-=1
                else:
                    j+=1
        return [ list(i) for i in ans]