class Solution:
    def isValid(self, s: str) -> bool:
        op = []
        clo = []
        brcs = {'[': ']',
                '{': '}',
                '(': ')'}
        for i in s:
            if (i in brcs.keys()):
                op.append(i)
            else:
                if (op and i == brcs[op.pop()]):
                    pass
                else:
                    return False
        if (op):
            return False
        return True