#link: https://leetcode.com/problems/tuple-with-same-product
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        freq={}
        for i in range(n):
            for j in range(i+1,n):
                prod=nums[i]*nums[j]
                if prod not in freq:
                    freq[prod]=1
                else:
                    freq[prod]+=1
        for val in freq:
            if freq[val]>=2:
                ans+=freq[val]*(freq[val]-1)//2
        return ans*8
        
