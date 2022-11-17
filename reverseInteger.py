class Solution():

    def reverse(self,x:int) -> int :
            
        if x<0 and x>=-2147483647 and x<=2147483647:
            splitted=str(x).split('-')
            res=int('-'+"".join(list(map(str,reversed(splitted[1])))))
            if res >=-2147483647:
                return res 
            return 0

        elif x>=-2147483647 and x<=2147483647:
            res=int("".join(list(map(str,reversed(str(x))))))
            if res<=2147483647:
                return res 
            return 0

        return 0


x=-12312312312312
print(Solution().reverse(x))


    