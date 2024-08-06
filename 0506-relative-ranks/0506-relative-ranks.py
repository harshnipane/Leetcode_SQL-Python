class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dct ={}
        s = sorted(score,reverse= True)
        for i in range(len(s)):
            if(i == 0):
                dct[s[i]] = "Gold Medal"
            elif(i == 1):
                dct[s[i]] = "Silver Medal"
            elif(i == 2):
                dct[s[i]] = "Bronze Medal"  
            else:
                dct[s[i]] = str(i+1)
        lt = []        
        for i in score:
            lt.append(dct[i])
        return lt