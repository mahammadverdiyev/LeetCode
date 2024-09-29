class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = list(nums)
        for i in range(len(nums)):
            current = l[i]
            target_index = (i + k) % len(nums)
            nums[target_index] = current
        

