class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l=0
        r=len(matrix)-1
        Row=None

        while l<=r:
            mid=(l+r)//2

            if matrix[mid][0]==target or matrix[mid][-1]==target:
                return True
            elif matrix[mid][0]<target and matrix[mid][-1]>target:
                Row=matrix[mid]
                break
            elif matrix[mid][0]>target:
                r=mid-1
            else:
                l=mid+1
        
        if Row is None:
            return False
        
        l=0
        r=len(Row)-1

        while l<=r:
            mid=(l+r)//2

            if Row[mid]==target:
                return True
            elif Row[mid]>target:
                r=mid-1
            else:
                l=mid+1
        
        return False