class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        
        for n in nums1:
            d[n] = d.get(n,0) + 1

        
        res = []
        for n in nums2:
            if d.get(n,0) != 0:
                res.append(n)
                d[n] = d.get(n) - 1

        return res