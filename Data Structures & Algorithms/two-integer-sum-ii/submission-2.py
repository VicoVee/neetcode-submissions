class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1

        # native, n^2
        for i in range(len(numbers)):
            for i in range(right):
                if(numbers[left] + numbers[right] == target):
                    return [left + 1, right + 1]
                else: 
                    left += 1
            left = 0
            right -= 1