class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if not nums:
            return 0
        
        k = 0
        while k < len(nums):
            if nums[k] == val:
                for i in range(k+1, len(nums)):
                    if nums[i] != val:
                        nums[k], nums[i] = nums[i], nums[k]
            if nums[k] == val:
                return k
            k += 1
        
        return k

        


