class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        maxi= 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            for j in range(i,len(s)):
                if(s[j] not in lst):
                    lst.append(s[j])
                else:
                    if(len(lst) > maxi):
                        maxi= len(lst)
                    lst =[]
                    break
        return maxi 