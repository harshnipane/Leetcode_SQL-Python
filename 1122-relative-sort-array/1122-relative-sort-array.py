class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dct = Counter(arr1)
        print(dct)
        arr3 = []
        for i in arr2:
                arr3.extend([i]*dct[i])

        arr1.sort()
        print(arr1)
        for i in arr1:
            if(i not in arr2):
                arr3.append(i)

        return arr3        


