class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper (x , n):
            if x == 0 : return 0   
            if n == 0 : return 1

            result = helper(x , n // 2)
            if n % 2 == 0 :
                return result * result
            else : 
                return x * result * result
        result = helper(x , abs(n))
        if n > 0 :
            return result
        else :
             return 1 / result

      
    # if n ==0 :
    # return 1
    # return  X * self.myPow(x , n-1)

          
     
        


        
        