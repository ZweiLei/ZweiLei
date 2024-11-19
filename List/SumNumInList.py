def sum2(nums: list) -> int:
    l = len(nums)
    cal = 0
    if l == 0:
        return 0
    elif l == 1:
        return nums[0]
    else:
        for i in range(2):
            cal += nums[i]
    return cal

if __name__ == "__main__":
    #输入数据
    nums = eval(input("please enter a num list: "))
    #调用函数测试并打印
    print(sum2(nums))