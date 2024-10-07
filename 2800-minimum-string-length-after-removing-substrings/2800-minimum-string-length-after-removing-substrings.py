class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for ch in s:
            if ch == 'B' and stack and stack[-1] == 'A':
                stack.pop()
            elif ch == 'D' and stack and stack[-1] == 'C':
                stack.pop() 
            else:
                stack.append(ch)  
                
        return len(stack)
