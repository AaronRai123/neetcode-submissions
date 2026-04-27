class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Sort the list to make duplicates adjacent
        for i in range(len(nums) - 1):  # Iterate through indices
            if nums[i] == nums[i + 1]:  # Check for duplicates
                return True  # Return True if duplicate is found
        return False  # Return False if no duplicates are found