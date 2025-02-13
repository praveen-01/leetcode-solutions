#link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans=0
        while len(nums)>=2:
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            if a>=k and b>=k:
                break
            temp=min(a,b)*2 + max(a,b)
            heapq.heappush(nums,temp)
            ans+=1
        return ans
        

        
