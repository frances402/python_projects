class Solution(object):
    def countOdds(self, low, high):
        num = (high - low) // 2
        if (high % 2 == 0) & (low % 2 == 0):
            return num
        else:
            return num + 1

print(Solution().countOdds(3,7))
print(Solution().countOdds(7,9))