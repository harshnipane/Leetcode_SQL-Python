class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        cnt = Counter(s)
        c=0
        for i in cnt.values():
            if(i %2 == 0):
                ans += i
            else:
                c=1
                ans += (i -1)

        if(c ==1):
            ans +=1
        return ans    
