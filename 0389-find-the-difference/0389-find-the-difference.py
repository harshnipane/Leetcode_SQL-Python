class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t1 = list(t)
        for i in s:
            t1.remove(i)

        return  t1[0]   