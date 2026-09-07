class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # off the bat, two pointer
        # for each pointer, calculate the height and width of the pool

        # Time Complexity O(N) Space Complecity ON

        maxVolume = 0
        l = 0 
        r = (len(heights)-1)

        while (l < r):
            # calculate current volume
            minHeight = min(heights[l], heights[r])
            volume = minHeight * (r-l)
            
            maxVolume = max(volume, maxVolume)

            # Real question, when to move left or right?
            # whatever the shortest one I will move

            if(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1

        return maxVolume

            

        