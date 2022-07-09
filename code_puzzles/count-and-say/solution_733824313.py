import numpy as np
class Solution:
    def countAndSay(self, n: int) -> str:
        res = 1
        if (n == 1):
             return('1')
        if (n == 2):
             return('11')
        res = 11
        for m in range(3,n+1):
            res = self.say(int(res))
        return(res)
            
    def say(self, n: int) -> str:
        chgng = np.insert(np.diff([int(d) for d in str(n)]) != 0, 0, False)
        cntd = np.ones(len(chgng))
        i = 0
        while (i < len(chgng)):
            j = i
            k = 0
            while ((j < len(chgng) - 1) and (not chgng[j+1])):
                j += 1
                k += 1
            cntd[i:j+1] = cntd[i:j+1] + k
            i = j
            i += 1
        chgng[0] = True  # small trick to get rid of
        eachdigit = np.array(list(str(n)))[chgng]  # saying: count + digit
        eachcount = cntd[chgng]
        out = ''.join([str(int(i)) for i in list(sum(zip(eachcount, eachdigit), ()))])
        return(out)
   