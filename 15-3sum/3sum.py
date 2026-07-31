class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set=set()
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                triplet=(nums[i],nums[l],nums[r])
                t_sum=sum(triplet)
                if t_sum==0:
                    result_set.add(triplet)
                    l+=1
                    r-=1
                elif t_sum>0:
                    r-=1
                else:
                    l+=1
        return list(result_set)

            
           