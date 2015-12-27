class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        if len(words)==0 or len(words)==1:
            return 0
        def len_compare(x, y):
            return len(y) - len(x)
        words = sorted( words, cmp = len_compare )
        masks = [0 for _ in xrange(len(words))]
        for i in xrange(len(words)):
            for letter in words[i]:
                masks[i] |= 1<<(ord(letter)-ord('a'))
        ret = 0
        for i in xrange(len(words)):
            if len(words[i])**2<ret:continue
            for j in xrange(i+1, len(words)):
                if masks[i]&masks[j]==0:
                    ret = max(ret, len(words[i])*len(words[j]))
                    break
        
        return ret
