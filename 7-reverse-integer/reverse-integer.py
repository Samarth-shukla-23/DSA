class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        rtype=0
        while x>0:
            rtype= rtype*10+x%10
            x=x//10
        rtype= sign*rtype
        if rtype<-2**31 or rtype>2**31-1:
            return 0
        return rtype


            