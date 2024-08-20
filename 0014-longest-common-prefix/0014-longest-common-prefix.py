class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in strs[1:]:
            k=0
            j=0
            while(j<min(len(ans),len(i)) and i[j] == ans[j]):
                k+=1
                j+=1
            ans = ans[:k]                   
        return ans