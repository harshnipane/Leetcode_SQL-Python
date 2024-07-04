# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        strt = 1
        end = n
        while(strt < end):
            mid = (strt + end)//2
            print(mid)
            if(guess(mid) <=0):    
                end = mid
            else:
                strt = mid+1

        return strt        
