class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals)==0: return [newInterval]
        intervals.append(newInterval)
        return self.merge(intervals)
        
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
