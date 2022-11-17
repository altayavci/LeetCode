#This problem includes topics that divide and conquer , dynamic programming and array.


class Solution:

    def maxSubArray(self,nums,left=None,right=None) -> int:

        if not nums : 
            #burası nums =[] olursa çalışacak bu bizim base conditionumuz. 
            return False  

        if left is None and right is None :
            #arraylerin lenghtini tespit etmek için
            left,right=0,len(nums)-1

        if right==left:
            #liste 1 veya 0 eleman barındırırsa 
            return nums[left]

        middle=(left+right)//2
        leftMax=-1000000000
        totalSum=0

        for i in range(middle,-1,-1):
            #soldaki subarray için max bulma 
            totalSum+=nums[i]

            if totalSum>leftMax:

                leftMax=totalSum

        rightMax=-1000000000
        totalSum=0

        for j in range(middle+1,right+1):
            #sağdaki subarray için max bulma 
            totalSum+=nums[j]

            if totalSum>rightMax:

                rightMax=totalSum

        maxLeftRight=max(self.maxSubArray(nums,left,middle),self.maxSubArray(nums,middle+1,right))

        return max(maxLeftRight,leftMax+rightMax)


    

    def maxSubArray2(self,nums,left=None,right=None):

        if not nums :

            return False 

        if left is None and right is None :

            left,right=0,len(nums)

        if right==left :

            return nums[left]


        middle=(left+right)//2
        leftMax=-1000000000
        totalSum=0

        


        


print(Solution().maxSubArray([1,2,3,4]))
        
    
