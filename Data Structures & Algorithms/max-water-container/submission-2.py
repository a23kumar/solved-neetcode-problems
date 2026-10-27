class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we can utilize a two pointer approach
        
        # volume can be calculated by:
        # min(heights[l], heights[r]) * (r - l - 1)
        max_vol = 0
        l, r = 0, len(heights) - 1

        while l < r:
            vol = min(heights[l], heights[r]) * (r - l)
            max_vol = max(max_vol, vol)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_vol
