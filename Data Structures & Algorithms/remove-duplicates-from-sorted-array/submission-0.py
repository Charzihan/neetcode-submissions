class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = 0
        head = 0
        dyna_len = len(nums) - 1
        i = 0
        while i < dyna_len:
            dup = nums[i]
            head = nums[i+1]
            while head == dup:
                nums.remove(dup)
                if i+1 != dyna_len:
                    head = nums[i+1]
                else:
                    break
                dyna_len -= 1
            i += 1

        return len(nums)