class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sorted by increase
        # No hashmaps, additional space of O(n), needs O(1)
        # We have to find two numbers to add up
        # Usually hold one and find the other, else increase and repeat '

        for i, a in enumerate(numbers):
            l = i 
            r = len(numbers) - 1

            while (l < r):
                tmp = numbers[l] + numbers[r]
                
                if(tmp == target):
                    return [l+1, r+1]
                elif(tmp < target): 
                    l += 1
                elif (tmp >= target):
                    r -= 1

        return []