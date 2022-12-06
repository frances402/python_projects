class Solution(object):
    def average(self, salary):
        salary.remove(min(salary))
        salary.remove(max(salary))
        return float(sum(salary))/len(salary)


salary = [4000,3000,1000,2000]
print(Solution().average(salary))
salary = [1000,2000,3000]
print(Solution().average(salary))
