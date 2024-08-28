class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_closers = {
            '}': '{', 
            ']': '[', 
            ')': '('
        }
        if len(s) %2 != 0:
            return False
        for i in s:
            if not stack and i in open_closers:
                print(stack, i, 'Closer before opener')
                return False
            if i in open_closers and open_closers[i] != stack[-1]:
                print('incorrect match')
                return False
            
            if i in open_closers and stack[-1] == open_closers[i]:
                stack.pop()
            else:
                stack.append(i)
            
        return True if not stack else False

