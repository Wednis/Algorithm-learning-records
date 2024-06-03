def sortArray(nums):
    for i in range(len(nums) - 1):
        flag = False    #是否发生交换的标志位
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:       #如果进行了冒泡后flag还是false说明已经是排序好的结果了
            break
    return nums

nums = [5,2,3,6,1,4]
print(sortArray(nums))
