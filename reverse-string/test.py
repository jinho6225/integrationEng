import unittest
from reverse_string import Solution

class Test(unittest.TestCase):

    """pass case"""
    def test_1(self):
        self.assertEqual(Solution.reverseParentheses(self, "ta()usw((((a))))"), 'tauswa')

    def test_2(self):
        self.assertEqual(Solution.reverseParentheses(self, "(abcd)"), 'dcba')

    def test_3(self):
        self.assertEqual(Solution.reverseParentheses(self, "(u(love)i)"), "iloveu")

    def test_4(self):
        self.assertEqual(Solution.reverseParentheses(self, "(ed(et(oc))el)"), 'leetcode')

    def test_5(self):
        self.assertEqual(Solution.reverseParentheses(self, "a(bcdefghijkl(mno)p)q"), 'apmnolkjihgfedcbq')

    def test_6(self):
        self.assertNotEqual(Solution.reverseParentheses(self, "(u(love)i)"), 'ievolu')

    def test_7(self):
        self.assertNotEqual(Solution.reverseParentheses(self, "(ed(et(oc))el)"), 'edetocel')

    """fail case"""
    """square bracket"""
    def test_8(self):
        self.assertEqual(Solution.reverseParentheses(self, "(u[love]i)"), 'iloveu')
    """not pair of matching parentheses"""
    def test_9(self):
        self.assertEqual(Solution.reverseParentheses(self, "(ed(et((oc))el)"), 'leetcode')


if __name__ == "__main__":
    unittest.main()
