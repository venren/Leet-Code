#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return sum(nums)

        iterator = 0
        maxEnd = 0
        currentSum = -100000
        maxSum = -100000

        while iterator < len(nums):
            newSum = currentSum + nums[iterator]

            if newSum > nums[iterator]:
                maxEnd += 1
                currentSum = newSum
            else:
                maxEnd = iterator
                currentSum = nums[iterator]

            if currentSum > maxSum:
                maxSum = currentSum

            iterator += 1

        return maxSum


Sol = Solution()
print(Sol.maxSubArray([-2,-1])) #-1
print(Sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
print(Sol.maxSubArray([5,4,-1,7,8])) #23
print(Sol.maxSubArray([1])) #1

