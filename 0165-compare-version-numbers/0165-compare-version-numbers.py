class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v11 :int
        v22 :int
        for i in range(max(len(v1), len(v2))):
            if i < len(v1):
                v11 = int(v1[i])
            else:
                v11 = 0
            if i < len(v2):
                v22 = int(v2[i]) 
            else:
                v22 = 0   

            print(v11,v22)
            if(v11> v22):
                return 1
            if(v11 < v22):
                return -1
        return 0     
