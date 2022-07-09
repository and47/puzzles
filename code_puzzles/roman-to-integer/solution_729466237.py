class Solution:
    def romanToInt(self, s: str) -> int:
        ito1 = {'I':             1,
                'V':             5,
                'X':             10,
                'L':             50,
                'C':             100,
                'D':             500,
                'M':             1000}
        pairs = {'IV':             4,
                 'IX':             9,
                 'XL':             40,
                 'XC':             90,
                 'CD':             400,
                 'CM':             900}
        searchforpairs = True
        out = 0
        while (searchforpairs):
            searchforpairs = False
            for p, num in pairs.items():
                if p in s:
                    s = re.sub(p, '', s, 1)
                    out += num
                    searchforpairs = True
        while(len(s) > 0):
            for l in s:
                s = re.sub(l, '', s, 1)
                out += ito1[l]
        return(out)
                