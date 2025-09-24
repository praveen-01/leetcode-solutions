class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast==slow:
                break
        ptr1 = nums[0]
        ptr2 = fast
        while ptr1!=ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
