class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator==0:
            return "0"
        
        res = []
        res.append('-' if (numerator>0) ^ (denominator>0) else '')
        
        num = abs(numerator);den = abs(denominator)
        #Integer part
        res.append( str(int(num/den)) )
        rem = num % den
        if rem==0:
            return "".join(res)
        
        res.append('.')
        
        dict = {}
        dict[rem] = len(res)
        
        while rem:
            rem *= 10
            res.append( str(int(rem/den)) )
            rem %=den
            if dict.has_key(rem):
                index = dict[rem]
                res.insert(index, '(')
                res.append(')')
                break
            else:
                dict[rem] = len(res)
                
        return "".join(res)
