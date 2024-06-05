#自己写的，不过有两个for
def find(nums):
    left = 0
    right = 0
    for i in range(len(nums)-2):
        left += nums[i]
        for j in range(len(nums)-i-2):
            right += nums[i+j+2]
        if left == right:
            return i+1
        right = 0
    return -1

#借鉴，这个只有一个for
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum * 2 + nums[i] == sum:
                return i
            curr_sum += nums[i]
        return -1
