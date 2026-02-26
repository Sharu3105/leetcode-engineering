import collections

class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            # Create a count of 26 zeros for a-z
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Use tuple of counts as key because lists are not hashable
            ans[tuple(count)].append(s)
        return list(ans.values())
