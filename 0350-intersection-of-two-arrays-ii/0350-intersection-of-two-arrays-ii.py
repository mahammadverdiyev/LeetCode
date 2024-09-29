class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        
        # optimizing memory
        small = nums1 if len(nums1) < len(nums2) else nums2
        big = nums1 if len(nums1) > len(nums2) else nums2

        if len(nums1) == len(nums2):
            small = nums1
            big = nums2


        for n in small:
            d[n] = d.get(n,0) + 1


        res = []
        for n in big:
            if d.get(n,0) != 0:
                res.append(n)
                d[n] = d.get(n) - 1

        return res