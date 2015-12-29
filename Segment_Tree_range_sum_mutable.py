class STNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = 0

    

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self.buildST(nums, 0, len(nums)-1)
        
    def buildST(self, nums, start, end):
        if start>end:
            return None
        root = STNode(start, end)
        
        if start==end:
            root.sum = nums[start]
        else:
            mid = (start + end)/2
            root.left = self.buildST(nums, start, mid)
            root.right= self.buildST(nums, mid+1, end)
            root.sum = root.left.sum + root.right.sum
        
        return root

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.ud(self.root, i, val)
        
    def ud(self, root, pos, val):
        if root.start == root.end:
            root.sum = val
        else:
            mid = (root.start + root.end)/2
            if pos <= mid:
                self.ud(root.left, pos, val)
            else:
                self.ud(root.right,pos, val)
            root.sum = root.left.sum + root.right.sum
            
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sr(self.root, i, j)
    def sr(self, root, start, end):
        if root.end ==end and root.start==start:
            return root.sum
        else:
            mid = (root.start + root.end)/2
            if end<=mid:
                return self.sr(root.left, start, end)
            elif start >= mid+1:
                return self.sr(root.right, start, end)
            else:
                return self.sr(root.right, mid+1, end) + self.sr(root.left, start, mid)
