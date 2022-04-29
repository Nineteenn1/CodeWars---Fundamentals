'''
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)
'''
from math import sqrt
def find_next_square(sq):
    return  (sqrt(sq)+1)*(sqrt(sq)+1) if ((sqrt(sq)+1)*(sqrt(sq)+1)).is_integer() else -1
