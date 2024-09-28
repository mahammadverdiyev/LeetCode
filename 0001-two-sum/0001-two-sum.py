class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [1,2,5,6,6,8]   target = 9
        # set = {8, 7, 4, }
        # dictionary = {8:0, 7:1, 4:2, 3:4, }
        
        needed_values = dict()

        for i in range(len(nums)):
            if nums[i] in needed_values:
                return [i, needed_values[nums[i]]]
            
            needed_values[target - nums[i]] = i

            
