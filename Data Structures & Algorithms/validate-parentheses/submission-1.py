class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        pairs = { '[': ']', '{': '}', '(': ')'}
        
        for ch in s:
            if (ch in pairs):
                myStack.append(ch)
            elif(ch in pairs.values()):
                if(len(myStack) != 0 and pairs.get(myStack[-1]) == ch):
                    myStack.pop()
                else:
                    return False
        
        return len(myStack) == 0 