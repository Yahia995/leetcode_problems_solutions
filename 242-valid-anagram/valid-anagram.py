class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        m1, m2 = {}, {}
        for i in range(len(s)):
            m1[s[i]] = 1 + m1.get(s[i], 0)
            m2[t[i]] = 1 + m2.get(t[i], 0)
        for c in m1:
            if m1[c] != m2.get(c, 0):
                return False
        return True