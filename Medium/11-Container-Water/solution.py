class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_res = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_res = max(max_res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_res
