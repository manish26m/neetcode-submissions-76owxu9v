class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif len(stack)!=0 and stack[-1] == mapping[ch]:
                stack.pop()
            else:
                return False

        if len(stack)==0:
            return True
        else:
            return False