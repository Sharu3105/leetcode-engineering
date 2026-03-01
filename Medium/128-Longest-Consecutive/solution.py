class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        
        for n in nums:
            # Check if it's the start of a sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
