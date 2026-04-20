class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_temp = [x for x in nums if x != val] # Modify in place
        nums[:] = nums_temp
        return len(nums)