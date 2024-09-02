class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bracket_stack = []
        # Recursive loop rules:
        # n  <= amount of possible opens
        # close count must be < open count to choose close
        # Pop stack after each char addition because we will only build our stack once base condition met
        res = []
        def makeBrackets(open_c, close_c):
            if open_c == close_c == n:
                res.append(''.join(bracket_stack))
                #Return here will revert state back to start allowing more possibilities
                return
            if open_c < n:
                bracket_stack.append('(')
                makeBrackets(open_c +1, close_c)
                #Pop the stack - if this state is called again it can rerun with clean slate
                bracket_stack.pop()
            if close_c < open_c:
                bracket_stack.append(')')
                makeBrackets(open_c, close_c +1)
                bracket_stack.pop()
        makeBrackets(0,0)
        return res        
