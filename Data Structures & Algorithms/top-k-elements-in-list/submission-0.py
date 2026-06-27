class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a hashmap to collect the count

        myMap = defaultdict(int)
        res = []

        for num in nums:
            myMap[num] += 1

        for i in range(k):
            ansKey = max(myMap, key=myMap.get)
            res.append(ansKey)

            # remove the previous max 
            myMap.pop(ansKey)

        return res


