#link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits
class Solution:
    def digit_sum(self,num):
        ans=0
        while num>0:
            rem=num%10
            ans+=rem
            num=num//10
        return ans
    def maximumSum(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            temp=self.digit_sum(i)
            if temp in d:
                d[temp].append(i)
            else:
                d[temp]=[i]
        ans=-1
        for i in d:
            if len(d[i])>1:
                temp=d[i]
                temp.sort()
                res=temp[-1]+temp[-2]
                ans=max(ans,res)
        return ans

        
