
class Solution:

    def combinations(self,iterable, r=3):
        pool = tuple(iterable)
        n = len(pool)
        indices = list(range(r))
        temp=list(pool[i] for i in indices)
        if sum(temp)==0:
                yield sorted(temp)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            temp=list(pool[i] for i in indices)
            if sum(temp)==0 :
                yield sorted(temp)

    def threeSum(self, nums: list) -> list :

        return list(set(map(lambda i: tuple(i),self.combinations(nums))))



nums=[-6,14,-11,7,-5,-8,12,-13,-3,-14,7,0,-7,-15,-5,-9,-13,-7,-5,9,8,-13,-6,-8,-12,7,-10,11,8,-14,12,9,-15,-14,1,-5,-7,-10,-10,5,-9,12,12,-1,12,14,-2,-15,-8,0,9,7,2,10,14,-3,2,11,-6,-13,12,13,11,5,14,-11,7,14,-6,12,-4,-7,9,-7,-1,-1,-8,4,-9,-9,-11,-15,5,6,10,4,11,-10,-8,12,-8,-10,10,11,2,9,-15,-14,0,-13,14,11,-5,0,-11,1,6,-12]
print(Solution().threeSum(nums))

