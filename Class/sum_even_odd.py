class nums:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list
    
    def get_even(self):
        even = [i for i in self.numbers_list if i % 2 == 0]
        return even

    def get_odd(self):
        odd = [i for i in self.numbers_list if i % 2 == 1]
        return odd

#def calculate_sum(numbers_list):
    # 此处编写代码 

# 获取输入转为列表
if __name__ == "__main__":

    numbers_list = list(map(int,input().split()))
    num1 = nums(numbers_list)

    print([sum(num1.get_even()), sum(num1.get_odd())])
# 打印偶数和奇数的和
#print(calculate_sum(numbers_list))