def rotate(nums, k: int):
    n = len(nums)
    k = k % n                #k不定，所以取余
    reverse(nums, 0, n-1)    #整个列表翻转
    reverse(nums, 0, k-1)    #从0到k-1（包含该元素）个元素进行翻转
    reverse(nums, k, n-1)    #从k到n-1（包含该元素）个元素进行翻转
    return nums
def reverse(nums, left: int, right: int):     #翻转
    while left < right :
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1
nums = [1,2,3,4,5]
print(rotate(nums=nums, k=2))
