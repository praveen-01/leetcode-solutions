class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        for i in range(len(height)):
            if not leftMax:
                leftMax.append(height[i])
            else:
                leftMax.append(max(height[i],leftMax[-1]))
        rightMax = []
        for i in range(len(height)-1,-1,-1):
            if not rightMax:
                rightMax.append(height[i])
            else:
                rightMax.append(max(height[i],rightMax[-1]))
        rightMax = rightMax[::-1]
        res = 0
        for i in range(len(height)):
            res+=min(leftMax[i],rightMax[i])-height[i]
        return res