class Solution(object):
    # O(nlogn) alg based on binary search
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in xrange(len(nums))]
        length = 0
        for item in nums:
            #print item
            #print dp
            #print length
            i = self.bs(dp, item, 0, length) 
            #print "i is"+str(i)
            dp[i] = item
            if i==length: length+=1
        return length
        
    def bs(self, arr, searchValue, left, right):
        if left>=right: return right
        while left<right:
            mid = (left + right) / 2
            if searchValue > arr[mid]:
                left = mid+1
            elif searchValue < arr[mid]:
                right = mid
            else:
                return mid
        return left
