class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Natively, just do a n*n for loop

        # One thing that strikes to me is the 32 bit integer
        # the highest number that can represent is 2^32 - 1 right?
        # some sort of bit manipulation?

        results = []
        # Implement native approach first
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                # if the index are not the same then proceed
                if j != i:
                    product *= nums[j]
            print(product)
            results.append(product)
        
        return results
            