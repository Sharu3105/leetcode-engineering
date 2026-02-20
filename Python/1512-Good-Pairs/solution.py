class Solution:
    def numIdenticalPairs(self, nums):
        count_dict = {}
        ans = 0
        
        for num in nums:
            if num in count_dict:
                ans += count_dict[num]
                count_dict[num] += 1
            else:
                count_dict[num] = 1
                
        return ans
