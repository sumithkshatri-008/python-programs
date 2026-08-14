class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]
        s=0
        for i in nums:
            s+=i
            prefix.append(s)
        for i in range(len(nums)):
            leftsum=prefix[i]
            rightsum=prefix[len(nums)]-prefix[i+1]
            if leftsum==rightsum:
                return i
        return -1
        
    
        