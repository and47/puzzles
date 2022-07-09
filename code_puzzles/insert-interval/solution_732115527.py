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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s_points = [i[0] for i in intervals]
        if (len(intervals) > 0):
            pos = binSearch(newInterval[0], s_points)
            while((len(intervals) > pos) and (newInterval[1] >= s_points[pos])):
                newInterval[1] = max(newInterval[1], intervals[pos][1])
                del s_points[pos]
                del intervals[pos]
            while((len(intervals) > 0) and (pos > 0) and (newInterval[0] <= intervals[pos-1][1])):
                newInterval[0] = min(newInterval[0], intervals[pos-1][0])
                newInterval[1] = max(newInterval[1], intervals[pos-1][1])
                del s_points[max(pos-1, 0)]
                del intervals[max(pos-1, 0)]
                pos -= 1
        else:
            pos = 0
            
        out = [*intervals[:pos], newInterval, *intervals[pos:]]
        return(out)    
        