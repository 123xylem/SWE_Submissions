class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init result with 0's
        # while current top of stack is < current temp
        # get index diff == (curr temp idx - curr stack idx) with repeated pops
        # the result will then be updated with how many indexes needed until larger num
        res = [0] * len(temperatures)
        stack = [] #[temp, indx]
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                s_temp, s_idx = stack.pop()
                res[s_idx] = (idx - s_idx)            
            stack.append([temp, idx])

        return res

