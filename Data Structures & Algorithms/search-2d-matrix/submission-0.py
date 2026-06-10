class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        fc=[row[0] for row in matrix]

        l=0
        r=len(fc)-1

        while l<=r:
            mid=(l+r)//2
            if fc[mid]>target:
                r=mid-1
            elif fc[mid]<target:
                l=mid+1
            else:
                return True
        
        if r<0 or r>len(matrix)-1:
            return False
        
        row=matrix[r]
        l=0
        r=len(row)-1

        while l<=r:
            mid=(l+r)//2
            if row[mid]>target:
                r=mid-1
            elif row[mid]<target:
                l=mid+1
            else:
                return True
        return False

        