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
        cand = None; count = 0
        for item in nums:
            if count==0:
                cand = item; count+=1
            elif item==cand:
                count += 1
            else:
                count -= 1
        
        return cand
