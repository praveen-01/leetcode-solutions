class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[i]<=nums[mid]:
                if nums[i]<=target<=nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            elif nums[mid]<=nums[j]:
                if nums[mid]<=target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1
