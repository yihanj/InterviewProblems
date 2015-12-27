class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0 for _ in xrange(n)]
        for i in xrange(1,n+1):
            arr = self.toggle(arr,i)
            print arr
        return sum(arr)
        
    def toggle(self,arr, n):
        if n==1:
            res = [1 for _ in arr]
        else:
            res = [0**arr[i] if (i+1)%n==0 else arr[i] for i in xrange(len(arr))  ]
        return res
