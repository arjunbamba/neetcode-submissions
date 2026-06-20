class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curOnes, maxOnes = 0, 0
        for num in nums:
            if num == 1:
                curOnes += 1
                maxOnes = max(curOnes, maxOnes)
            else:
                curOnes = 0
        
        return maxOnes