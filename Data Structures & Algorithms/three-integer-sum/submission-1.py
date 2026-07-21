class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            a = nums[i]
            b = i + 1
            c = n - 1
            
            while b < c:
                val = a + nums[b] + nums[c]
                
                if val > 0:
                    c -= 1
                elif val < 0:
                    b += 1
                else:
                    ans.append([a, nums[b], nums[c]])
                    b += 1
                    c -= 1
                    
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                        
        return ans