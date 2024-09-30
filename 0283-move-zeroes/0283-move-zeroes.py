class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
        
        must_swipe = len(nums) - zero_count
        tracker = 0

        for i in range(len(nums)):
            current = nums[i]

            if must_swipe == 0:
                break

            if current != 0:
                nums[tracker] = current
                tracker += 1
                must_swipe -= 1
            
        for i in range(len(nums)-zero_count,len(nums)):
            nums[i] = 0


                


