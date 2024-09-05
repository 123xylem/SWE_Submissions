class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(i) for i in digits)
        s = int(s) + 1
        s = str(s)
        # print(s, s.split(''))
        return [int(x) for x in s]
        # if digits[-1] == 9:
        #     digits.append(0)
        # if digits[-2] == 9:
        #     digits[-2] = 1

        # for i, v in enumerate(digits[::-1]):
        #     if v == 9:
        #         digits[-1] = 1
        #         digits.append(0)

        #         digits[-1] = 1
        #         digits.append(0)
        # else:
        #     digits[-1] += 1
        return digits
