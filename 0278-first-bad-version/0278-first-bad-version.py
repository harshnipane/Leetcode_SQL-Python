# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1: return 1;
        st=1
        end=n
        while st<end:
            mid=st+(end-st)/2
            if isBadVersion(mid): 
                end=mid
            else: 
                st=mid+1
        return int(st)