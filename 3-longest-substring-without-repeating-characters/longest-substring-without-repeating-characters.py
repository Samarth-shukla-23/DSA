class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1=[]
        l2=[0]
        for char in s:
            if char in l1:
                dup_cindex=l1.index(char)
                l1=l1[dup_cindex+1:]
            l1.append(char)
            k=len(l1)
            l2.append(k)
        return max(l2)

        


