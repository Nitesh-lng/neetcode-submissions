class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_pd=1
        right_pd=1
        preffix=[1]*len(nums)
        suffix=[1]*len(nums)
        output=[]

        for i in range(len(nums)):
            preffix[i]=left_pd
            left_pd *=nums[i]

        for j in range(len(nums)-1, -1, -1):
            suffix[j]=right_pd
            right_pd *=nums[j]

        output=[pi*sj for pi,sj in zip(preffix,suffix)]
        return output