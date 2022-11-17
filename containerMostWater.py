import time 
class Solution():

    def maxArea(self,height:list)->int :

        heightWithIndex=dict(zip(range(len(height)),height))
        for descent in reversed(range(len(height))):
            for ascent in range(len(height)):
                if descent>ascent :
                    horizontal=descent-ascent
                    if heightWithIndex.get(ascent) >= heightWithIndex.get(descent):
                        vertical=heightWithIndex.get(descent)
                        area=vertical*horizontal
                        yield area 
                    else :
                        vertical=heightWithIndex.get(ascent)
                        area=vertical*horizontal
                        yield area
                        
    def maxArea2(self, height:list) -> int:
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l]<height[r]:

                l+=1 
            else :

                r-=1
				
        return area

height=[1,1,8,7,2,21,24,12,5,1,24,12,4,1,241,2,4,56,6,8780,8,786,5,8,5,57,4,3,4,12,124,1,1231,545,1,2,4,12,12,3,5,1,23,1,2,312,4,41,24,12,4,12,41,18899]
st1=time.time()
print(max(list(Solution().maxArea(height))))
fin1=time.time()

st2=time.time()
print(Solution().maxArea2(height))
fin2=time.time()

print(f'maxArea : {fin1-st1}, maxArea2: {fin2-st2}')
