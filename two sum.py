class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
if __name__=="__main__":
    a=Solution()
    nums=[3,3]
    target=6
    print(a.twoSum(nums,target))