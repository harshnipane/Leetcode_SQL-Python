class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 1):
            return s[0]
        maxi = 0
        pal =""
        for i in range(len(s)-1):
            for j in range(i+1,len(s)+1):
                s1 = s[i:j] 
                if(s1 == s1[::-1]):
                    if(len(s[i:j]) > maxi):
                        maxi = len(s[i:j])
                        pal = s[i:j]
        return pal    