
#In python , HASHTABLE equals to the dict data structure. 
#This two problems contains that hashatbles, dicts and math operators . It also includes basic list operations but mostly dict operations. 
#O(n*logn)

class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        sum_=0
        total_sum=0

        if len(s)==1:

            return symbols.get(s)

        else :

            for i in range(1,len(s)):

                prev,next_=s[i-1],s[i]
                total_sum+=symbols.get(prev)
    
                if prev=='C' or prev=='I' or prev=='X':

                    temp=prev+next_

                    if symbols.get(temp) !=None:

                        sum_-=symbols.get(prev)

                if i==len(s)-1:

                    total_sum+=symbols.get(s[-1])



            return total_sum+(sum_*2)


    def intToRoman(self, num: int) -> str:

        symbols={1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        num_digits=len(str(num))
        romans=[]
        num=str(num)[::-1] #reversed string 

        for i,digit in enumerate(num):

            digit_value=int(digit)*(10**i)
            num_digit=len(str(int(digit)*(10**i)))


            if digit=='0':

                continue
            

            if num_digit==4:

                if digit=='1' or digit=='2' or digit=='3' :

                    #print(symbols.get(1000)*int(digit))
                    romans.append(symbols.get(1000)*int(digit))

                else :

                    #print(symbols.get(digit_value))
                    romans.append(symbols.get(digit_value))

            elif num_digit==3:

                if digit=='1' or digit=='2' or digit=='3' :

                     #print(symbols.get(100)*int(digit))
                    romans.append(symbols.get(100)*int(digit))


                elif digit=='6' or digit=='7' or digit=='8':

                    #print(symbols.get(500)+(symbols.get(100)*(int(digit)-5)))
                    romans.append(symbols.get(500)+(symbols.get(100)*(int(digit)-5)))


                else :

                    #print(symbols.get(digit_value))
                    romans.append(symbols.get(digit_value))

            elif num_digit==2:

                if digit=='1' or digit=='2' or digit=='3' :

                    #print(symbols.get(10)*int(digit))
                    romans.append(symbols.get(10)*int(digit))


                elif digit=='6' or digit=='7' or digit=='8':

                    #print(symbols.get(50)+(symbols.get(10)*(int(digit)-5)))
                    romans.append(symbols.get(50)+(symbols.get(10)*(int(digit)-5)))


                else :

                    #print(symbols.get(digit_value))
                    romans.append(symbols.get(digit_value))
        
        

            else :

                if digit=='1' or digit=='2' or digit=='3' :

                    #print(symbols.get(1)*int(digit))
                    romans.append(symbols.get(1)*int(digit))


                elif digit=='6' or digit=='7' or digit=='8':

                    #print(symbols.get(5)+(symbols.get(1)*(int(digit)-5)))
                    romans.append(symbols.get(5)+(symbols.get(1)*(int(digit)-5)))


                else : 

                    #print(symbols.get(digit_value))
                    romans.append(symbols.get(digit_value))



       # romans=[item for sublist in romans for item in sublist]
        romans.reverse()
        return "".join(romans)




s=Solution().intToRoman(3768)
print('Integer ( {} )to Roman:'.format(3768),s)
print('Roman ( {} ) to integer :'.format(s),Solution().romanToInt(s))









        


















