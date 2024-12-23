#编写一个程序，确定给定字符串中子字符串的重复次数。

#定义函数repetitions_in_string()，该函数接受一个字符串参数。
#在函数中，返回提供的字符串中子字符串的重复次数。
#注意：如果字符串不是由单个子字符串重复形成的，则输出应为1。
#
#例如，在字符串pythonpropro中，子串pro重复了两次，但是这种重复本身不能形成完整的字符串。因此输出为1。

def repetitions_in_string(s):
    # 此处编写代码
    length = len(s)
    if length <= 1:
        return 1
    else:
        repetion_end = s[1:].find(s[0]) + 1
#        print(s[1:], repetion_end)
        repetion_string = s[:repetion_end]
#        print(repetion_string)
        repetion_num = s.count(repetion_string)
#        print(repetion_num)
        if repetion_num * len(repetion_string) == length:
            return repetion_num
        else:
            return 1


if __name__ == "__main__":
    # 获取输入 
    #test_string = input()

    # 调用函数 
    print(repetitions_in_string('dededededede') == 6)