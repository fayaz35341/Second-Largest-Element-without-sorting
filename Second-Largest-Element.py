class Solution:
    def secondLargestElement(self, nums):
        L=nums[0]
        SL=0
        for i in range(len(nums)-1):
            if (nums[i]<nums[i+1]) :
                SL=L
                L=nums[i+1]
                
            if L> nums[i]>SL:
                    SL=nums[i]
            elif L>nums[i+1]>SL:
                SL=nums[i+1]
        if SL==0:
            return '-1'
        return SL  

# class Solution:
#     def getSecondLargest(self, arr):
#         # Code Here
#         L=float('-inf')
#         SL=float('-inf')
#         for x in arr:
#             if x>L:
#                 SL=L 
#                 L=x
                
#             elif L>x >SL:
#                     SL=x
            
#         return '-1' if SL==float('-inf') else SL
n=[8, 8, 7, 6, 5]
print(Solution().largestElement(n))
