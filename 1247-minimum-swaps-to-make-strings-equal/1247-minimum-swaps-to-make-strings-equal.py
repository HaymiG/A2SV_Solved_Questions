class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = 0
        y_x = 0
        for i , j in zip(s1,s2):
            if i == "x" and j == "y":
                x_y += 1
            elif i == "y" and j == "x":
                y_x += 1
        if (x_y + y_x) % 2 == 1:
            return -1
        swap = x_y // 2 + y_x // 2
        if x_y % 2 == 1 :
            swap += 2
        return swap





        




        

        count 