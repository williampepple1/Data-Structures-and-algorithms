class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalSum = 0
        maxSum = nums[0]
        
        for i in nums:
            if finalSum < 0:
                finalSum = 0
            finalSum += i
            maxSum = max(maxSum, finalSum)
        return maxSum
        