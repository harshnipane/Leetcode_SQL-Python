class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt =0
        sh = sorted(heights)
        for i,j in zip(heights,sh):
            if(i != j):
                cnt+=1

        return cnt        