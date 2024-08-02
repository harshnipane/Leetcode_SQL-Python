class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split()  
        l1= []
        l2= []
        for i in pattern:
            l1.append(pattern.index(i))
        print(l1)
        for i in l:
            l2.append(l.index(i))
        print(l2)

        if l1==l2:
            return True
        else:
            return False 