def binSearch(k: int, seq: List[int]) -> int:
   mp = len(seq) // 2
   if ((k == seq[mp])): return(mp)
   if (mp == 0):
       pos = int(k > seq[mp])
   elif (k < seq[mp]):
       pos = binSearch(k, seq[:mp])
   else:
       pos = binSearch(k, seq[mp:]) + mp
   return(pos)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return(binSearch(target, nums))