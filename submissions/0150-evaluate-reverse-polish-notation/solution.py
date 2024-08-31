class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        curr_total = 0
        for i in tokens:
            if i not in {'+', '-', '*', '/'}:
                num_stack.append(i)
            else:
                math_str = str(num_stack[-2]) + str(i) + str(num_stack[-1])
                curr_total = int(eval(math_str))
                num_stack = num_stack[0:-2]
                num_stack.append(curr_total)
        return int(num_stack[0])
