'''
2. Reverse string
    Given a string s that consists of lower case English letters and brackets. 
    Reverse the strings in each pair of matching parentheses, starting from the innermost one.
    Your result should not contain any bracket.
    
    Example 1:
    Input: s = "(abcd)"
    Output: "dcba"
    Example 2:
    Input: s = "(u(love)i)"
    Output: "iloveu"
    Example 3:
    Input: s = "(ed(et(oc))el)"
    Output: "leetcode"
    Example 4:
    Input: s = "a(bcdefghijkl(mno)p)q"
    Output: "apmnolkjihgfedcbq"
    
    Constraints:
    0 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It's guaranteed that all parentheses are balanced.


    class Solution(object):
        def reverseStr(self, s):
            """
            :type s: str
            :rtype: str
            """
'''
'''
given test cast passed, but it cannot pass case below
"ta()usw((((a))))"
need to take care this case above
my code doesn't work for this case
need to resolve again

iterate string and append it into stack
    keep pushing until meet ")"
    if char is ")"
        pull out char into reverseArr list from stack until meet '('
        (it should be append it - in order to reverse character order)
        if char is '('
            cancat reverseArr with stack list
            and reverseArr assign as empty list
return stack element using join() method as string

'''

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """        
        stack = []
        reverseArr = []
        for i in range(0, len(s)):
            if s[i] == ')':
                char = stack.pop()
                while char != "(":
                    reverseArr.append(char)
                    char = stack.pop()
                stack = stack + reverseArr
                reverseArr = []
                
            else:
                stack.append(s[i])
        return ''.join(stack)

