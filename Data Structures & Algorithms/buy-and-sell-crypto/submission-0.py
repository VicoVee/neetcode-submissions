class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window 
        # Two pointers, one for the present day another for the future 
        # Can's sort since it is dependent on the order
        """
            On the left pointer, keep moving until you get the smallest price
            by using right pointer to check

            For the right, find the sell price by moving until you hit the smallest number again, which you will move the left pointer

        """


        left, right = 0,0 
        sellDay = 0
        maxProfit = 0 

        while right < len(prices):
            if(prices[left] > prices[right]):
                # Before switching, store the current profit
                maxProfit = max(maxProfit, prices[sellDay] - prices[left])

                # Then reset the pointer/window
                left = right
                sellDay = right 

            # Checks the best sell day    
            elif(prices[right] > prices[sellDay]):
                sellDay = right

            # Expand the Window
            right += 1
            
        # Check one more time before ending the loop
        maxProfit = max(maxProfit, prices[sellDay] - prices[left]) 
        return maxProfit 


        