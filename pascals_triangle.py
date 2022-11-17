#this problem included topics that array and dynamic programming. 

#pascal[2][1:-1]=[pascal[1][0]+pascal[1][1]]
#pascal[3][1:-1]=[pascal[2][0]+pascal[2][1],pascal[2][1]+pascal[2][2]]
#pascal[4][1:-1]=[pascal[3][0]+pascal[3][1],pascal[3][1]+pascal[3][2],pascal[3][2]+pascal[3][3]]

import time 

class Solution:

    def generate(self, numRows: int) -> list :

        pascal=[[1]*k for k in range(1,numRows+1)]

        for k in range(2,numRows):

            temp=pascal[k-1]
            for j in range(1,len(temp)) :

                prev,next=temp[j-1],temp[j]
                pascal[k][j]=prev+next

        return pascal


    def print_triangle(self,numRows):

        triangle=self.generate(numRows)

        for idx in range(len(triangle)-1,-1,-1):

            num_curr,num_next=len(triangle[idx]),len(triangle[idx-1])

            if idx==len(triangle)-1 :
                print(triangle[idx])
            else: 

                print(((11-idx)*' ')+''.join(str(triangle[idx]))+((11-idx)*' '))


        return 0

i=0
while i<5:

    times=[]
    st=time.time()
    x=Solution().print_triangle(10)
    fn=time.time()
    i+=1

    times.append(fn-st)

print(sum(times)/len(times))