class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # First store the character count in a hashmap
        # Do I create a list of hashmaps, then loop each word to compare the count
        # to the existing maps

        # Size O(M) 
        mainList = []
        isAdded = False

        # Time Complexity: 
        # O(N) + O(M)
        for i in range(len(strs)):
            word = strs[i]
            if(i == 0):
                mainList.append([word])
            else:
                for listItem in mainList:
                    if(sorted(listItem[0]) == sorted(word)):
                        listItem.append(word)
                        isAdded = True
                        break
                if(isAdded):
                    isAdded = False
                else:
                    mainList.append([word])
        
        
        return mainList

    