class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx_avg=-10000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            if right>=k-1:
                avg=currentsum/k
                mx_avg=max(mx_avg,avg)
                currentsum-=nums[left]
                left+=1
        return mx_avg
        