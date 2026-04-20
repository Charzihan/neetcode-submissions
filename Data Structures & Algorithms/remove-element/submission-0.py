class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val] # Modify in place
        # nums = nums_temp only assigns locally
        return len(nums)