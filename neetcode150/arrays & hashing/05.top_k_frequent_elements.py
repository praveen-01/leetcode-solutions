class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}
        for i in nums:
            if i not in freq_list:
                freq_list[i]=1
            else:
                freq_list[i]+=1
        bucket = [[] for i in range(len(nums)+1)]
        for i,val in freq_list.items():
            bucket[val].append(i)
        res= []
        for i in range(len(bucket)-1,-1,-1):
            for item in bucket[i]:
                res.append(item)
                if len(res)==k:
                    return res
        