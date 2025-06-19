from typing import List


class Solution:
    # def fizzBuzz(self, number: int) -> List[str]:
    def fizzBuzz(self, number):
        result_list = []
        r3=0
        r5=0
        for i in range(1, number + 1):
            result = ''
            r3 += 1
            r5 += 1
            if (r3 == 3) :
                r3 = 0
                result +='Fizz'
            if (r5 == 5) :
                r5 = 0
                result +='Buzz'
            if (result == ''):
                result +=str(i)
            result_list.append(result)
        return result_list

sol = Solution()
print(sol.fizzBuzz(30))