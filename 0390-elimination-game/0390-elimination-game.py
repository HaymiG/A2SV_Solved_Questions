class Solution:
    def lastRemaining(self, n: int) -> int:
       # x : current element
       #step : spacing between numbers
       # count : how many numbers remain 
       #direction : true l - r , fase r - l
        def helper(x, step, count, direction):
            if count < 2:
                return x
            increment = step if direction or count % 2 else 0
            return helper(x + increment, step * 2, count // 2, not direction)

        return helper(1, 1, n, True)

                

        