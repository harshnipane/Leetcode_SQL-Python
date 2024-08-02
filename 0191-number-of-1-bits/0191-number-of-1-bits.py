class Solution:
    def hammingWeight(self, n: int) -> int:
        l= []
        count =0
        while(n !=0):
            x =divmod(n,2) 
            n = x[0]
            if(x[1]==1 ):
                count+=1
        return count   