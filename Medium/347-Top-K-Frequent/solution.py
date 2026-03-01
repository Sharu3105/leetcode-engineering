import collections

class Solution:
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        # Create a list of lists where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        res = []
        # Move from highest frequency bucket to lowest
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
