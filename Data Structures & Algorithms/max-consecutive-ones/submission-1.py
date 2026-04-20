class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec, temp_consec = 0, 0

        for i in nums:
            if i == 1:
                temp_consec += 1
                max_consec = max(temp_consec, max_consec)
            else:
                temp_consec = 0

        return max(max_consec, temp_consec)
                
        