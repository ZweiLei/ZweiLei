def max_end3(nums):
    n = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = n
    return nums

if __name__ == "__main__":
    #Enter the data
    nums = eval(input("please enter a list with 3 numbers:"))
    #调用函数打印结果
    print(max_end3(nums))