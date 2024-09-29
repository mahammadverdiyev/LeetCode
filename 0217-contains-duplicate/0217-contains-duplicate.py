class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for val in nums:
            if val in num_set:
                return True
            else:
                num_set.add(val)
        
        return False
            