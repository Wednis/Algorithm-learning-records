#1.双循环
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(twoSum(nums = [2,7,11,15], target = 17))       #返回[0, 3]

#2.单循环，通过相减判断
def twoSum(nums: list[int], target: int) -> list[int]:
    numDict = dict()
    for i in range(len(nums)):
        if target-nums[i] in numDict:                #从头开始存入空字典，直到轮到循环时，差值能在字典中找到
            return numDict[target-nums[i]], i        #返回差值所在下标，和当前循环下标
        numDict[nums[i]] = i                         #通过字典赋予下标，使得与原来列表下标对应
    return [0]
print(twoSum(nums = [2,7,11,15], target = 17))

#数组较大时单循环优于双循环
