class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 - Brute Force
        # Time: O(n^2)
        # Memory: O(1)

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [-1, -1]

        # Solution 2 - Dictionary
        # Time: O(n)
        # Memory: O(n)

        sumMap = {}
        for i, n in enumerate(nums):
            if n in sumMap:
                return [sumMap[n], i]
            sumMap[target - n] = i
        return [-1, 1]