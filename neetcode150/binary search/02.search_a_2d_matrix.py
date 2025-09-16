class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m-1
        row_idx = -2
        while i<=j:
            mid = (i+j)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                row_idx = mid
                break
            elif matrix[mid][0]>target:
                j=mid-1
            else:
                i=mid+1
        if row_idx==-2:
            return False
        i = 0
        j = n-1
        while i<=j:
            mid = (i+j)//2
            if matrix[row_idx][mid]==target:
                return True
            elif matrix[row_idx][mid]>target:
                j = mid-1
            else:
                i = mid+1
        return False
