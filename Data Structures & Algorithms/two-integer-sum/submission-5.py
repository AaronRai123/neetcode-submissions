class Solution:
    def twoSum(self, nums, target):
        index_map = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                # Found the pair
                return [index_map[complement], i]
            # Store the index of the current number
            index_map[num] = i

