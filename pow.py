class Solution:
    def myPow(self, x: float, n: int) -> float:

        try :
            
            if n>=0:
                temp=None

                if n==0 :
                    return 1
        
                else :

                    temp=x
                    return  temp*self.myPow(temp, n-1)

            if n<0 :

                if n==0:

                    return 1

                else :

                    return 1/x*self.myPow(x,n+1)

        except RecursionError: 
            for k in range(n-2):

                temp*=temp

            return temp
            



  
sol=Solution().myPow(1.2312,998)

print(sol)





