class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(a[0]=='0' and b[0] == '0'):
            return "0"
        ab = int(a,2) + int(b,2)
        st = ""
        qt = ab
        while(qt > 0):
            qt = ab // 2
            rem = ab % 2
            ab = qt
            st += str(rem)
        return st[::-1]