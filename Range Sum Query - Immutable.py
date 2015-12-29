class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums)==0:
            self.code = []
            return
        code = [0 for _ in xrange(len(nums)+1)]
        for i in xrange(1,len(nums)+1):
            code[i] = code[i-1]+ nums[i-1]
        self.code = code

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.code[j+1]-self.code[i]
