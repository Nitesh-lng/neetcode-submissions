class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0
        
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            current_area = width * height

            if current_area > max_water:
                max_water = current_area
                
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_water