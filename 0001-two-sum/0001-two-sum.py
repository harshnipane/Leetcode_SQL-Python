class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        for i, e in enumerate(nums):
            rem = target - e
            if rem in d:
                return [d[rem], i]
            d[e] = i