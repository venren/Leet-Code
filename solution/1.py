from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        comparator = 1
        placer = 1
        while comparator < len(nums):
            if nums[comparator] == nums[comparator - 1]:
                comparator += 1
            else:
                nums[placer] = nums[comparator]
                placer += 1
                comparator += 1

        return placer

    def betterSolution(self, nums: List[int]) -> int:
        n = len(nums)
        return n - len([nums.pop(i) for i in range(n - 1, 0, -1) if nums[i] == nums[i - 1]])


my_numbers = [1, 1, 2, 3, 4, 4, 6, 6, 7, 7]
obj = Solution()
result = obj.betterSolution(my_numbers)
print("Result:", result)
print(my_numbers)
