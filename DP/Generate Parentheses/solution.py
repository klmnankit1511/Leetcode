"""
Question 

Link - https://leetcode.com/problems/generate-parentheses/description/

Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def utilsGenerateParenthesis(s: str , n: int, left: int, right: int, ans):
            if left == right and left == n:
                ans.append(s)
                return
            if left > n or right > n:
                return
            utilsGenerateParenthesis(s+"(",n,left+1,right,ans)
            if left >= right+1:
                utilsGenerateParenthesis(s+")",n,left,right+1,ans)
            return
        ans = []
        utilsGenerateParenthesis("",n,0,0,ans)
        return ans

sol = Solution()
brackets = sol.generateParenthesis(4)

for bracket in brackets:
    print(bracket, end = ", ")

"""

Input - 4
Output - (((()))), ((()())), ((())()), ((()))(), (()(())), (()()()), (()())(), (())(()), (())()(), ()((())), ()(()()), ()(())(), ()()(()), ()()()(),

"""