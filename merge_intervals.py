# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:return []
        res = []
        intervals.sort(key = lambda x: x.start)
        
        for item in intervals:
            if res and item.start <= res[-1].end:
                res[-1].end = max ( item.end, res[-1].end)
            else:
                res.append(item)
        return res
