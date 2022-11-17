import time 

class Solution:
    def getRow(self, rowIndex: int) :

        rowIndex=rowIndex+1

        pascal=[[1]*k for k in range(1,rowIndex+1)]

        for k in range(2,rowIndex):

            temp=pascal[k-1]
            for j in range(1,len(temp)) :

                prev,next=temp[j-1],temp[j]
                pascal[k][j]=prev+next

        return pascal[rowIndex-1]



    def print_triangle2(self,rowIndex):

        temp=None

        if rowIndex==0:

            return temp

        if rowIndex!=0:

            temp=self.getRow(rowIndex-1)

            print((11-rowIndex)*' ' + ''.join(str(temp)))

            return self.print_triangle2(rowIndex-1)

        return temp


i=0
while i<5:

    times=[]
    st=time.time()
    x=Solution().print_triangle2(10)
    fn=time.time()
    i+=1

    times.append(fn-st)

print(sum(times)/len(times))