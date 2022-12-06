class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagram = False
        full = set(s+t) # set doesn't allow duplicates
        if len(s) == len(t):
            for i in full:
                if s.count(str(i)) == t.count(str(i)):
                    anagram = True
                else:
                    return False
        return anagram
        #return sorted(s) == sorted(t)

print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))