class Solution:
    def addDigits(self, num: int) -> int:
        count = 0
        if(num == 0):
            return count
        if(len(str(num)) == 1):
            return num    
        while(len(str(num)) !=1):
            s = str(num)
            n = 0
            for i in s:
                n += int(i)
            num =n    
        return num