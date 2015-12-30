class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)==1 and t in s:
            return t
        need = collections.Counter(t)
        missing = len(t)
        i = I = J = 0
        
        for j in xrange(len(s)):
            missing -= need[s[j]]>0
            need[s[j]] -= 1
           
            if missing==0:
                while i<j and need[s[i]]<0:
                    need[s[i]] += 1
                    i+=1
                if J==0 or j-i <= J - I:
                    J, I = j, i
        if missing==0:
            return s[I:J+1]
        else:
            return ""
