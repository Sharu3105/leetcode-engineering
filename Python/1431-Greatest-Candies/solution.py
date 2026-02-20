class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        result = []
        
        for candy in candies:
            result.append(candy + extraCandies >= max_candy)
            
        return result
