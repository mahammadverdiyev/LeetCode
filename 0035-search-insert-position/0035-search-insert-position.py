class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums) - 1
        mid = 0
        midVal = 0
        while left <= right:
            mid = (right + left) // 2
            midVal = nums[mid]

            if midVal < target:
                left = mid + 1
            elif midVal > target:
                right = mid - 1
            else:
                return mid

        if target > midVal:
            return mid + 1
        else:
            return mid