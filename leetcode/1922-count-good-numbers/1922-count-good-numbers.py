class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        even_idx = (n+ 1) //2
        odd_idx = n // 2
        def pow(x , y):
            if y == 0 :
                return 1
            if y % 2 == 0 :
                half = pow(x , y // 2)
                return half * half % MOD
            else :
                return x * pow(x , y-1) % MOD
        return (pow(5 , even_idx)*pow(4 , odd_idx)) % MOD


        