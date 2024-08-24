class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        r0 =[1]
        r1 = [[1]] 
        for row in range(numRows-1):

            r = [1]
            for i in range(len(r0)):
                r.append(sum(r0[i:i+2]))
            r1.append(r)
            r0 = r
        return r1