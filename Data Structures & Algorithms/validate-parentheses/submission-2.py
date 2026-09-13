class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        pairs = {"}": "{", "]": "[", ")": "("}

        for ch in s: 
            if (pairs.get(ch) != None):
                if(len(myStack) != 0 and pairs[ch] == myStack[-1]):
                    myStack.pop()
                else: 
                    return False
            else:
                myStack.append(ch)

        return len(myStack) == 0