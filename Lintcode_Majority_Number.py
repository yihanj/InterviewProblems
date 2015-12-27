import random

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if nums==[]:
            return None
        
        rad = [ random.randint(0,len(nums)-1) for i in xrange(10)]
        res = [ nums[i] for i in rad]
        pi = {}
        for i in res:
            if i in pi:
                pi[i] +=1
            else:
                pi[i] = 1
        maxi = max(pi.values())
        for i in pi:
            if pi[i]==maxi:
                return i
        return nums[random.randint(0,len(nums-1))]
