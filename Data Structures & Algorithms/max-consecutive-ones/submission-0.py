class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = 0
        temp_consec = 0

        for i in nums:
            if i == 1:
                temp_consec += 1
            if temp_consec > max_consec:
                max_consec = temp_consec
            if i == 0:
                temp_consec = 0

        return max_consec
                
        