# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e., 0 <= i < n).

# In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

# Given an integer n, the length of the array, return the minimum number of operations needed to make all the elements of arr equal.

import math
from leetcode_test_runner import *

class Solution:
    def impl(n: int) -> int:
        max_delta = math.floor(n / 2) * 2
        num_pairs = math.ceil(n / 2) / 2
        return max_delta * num_pairs
    
    def minOperations(self, n: int) -> int:
        return self.impl(n)

testcases = [
    (6, 9),
# [1, 3, 5, 7, 9, 11]
# [5, 3, 1, 1, 3, 5]
# 9
    (7, 12)
# [1, 3, 5, 7, 9, 11, 13]
# [6, 4, 2, 0, 2, 4, 6]
# 12
]

run_tests(Solution, testcases)
        