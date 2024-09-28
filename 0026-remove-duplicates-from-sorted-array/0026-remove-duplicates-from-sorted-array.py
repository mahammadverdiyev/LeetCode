class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        tracker = 1
        for i in range(1,len(nums)):
            current = nums[i]
            if current == last:
                continue
            nums[tracker] = current
            last = current
            tracker += 1
        return tracker
            
            
               
        
