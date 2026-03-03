class Solution:
    def containsDuplicate(self, nums):
        # A Set only stores unique values. If length changes, there was a duplicate.
        return len(set(nums)) != len(nums)
