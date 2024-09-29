class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            d[n] = d.get(n,0)+1
        
        for key in d:
            if d[key] == 1:
                return key
        
        
        