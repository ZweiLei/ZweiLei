#编写一个程序，计算从两个字符串中移除的最少字母数，使它们成为变位词。

#变位词是指可以通过重新排列字符而形成的字符串。例如，dab 是 bad 的变位词。

#定义函数 min_removals_to_anagram()，有两个参数：str1 和 str2。
#在函数内，计算从两个字符串中移除的最小字母数，使它们成为变位词。
def min_removals_to_anagram(str1, str2):
    # 此处编写代码
    same_words = 0
    for i in str1:
        if i in str2:
            same_words += 1
    return len(str1) + len(str2) - 2 * same_words
# 获取输入 
if __name__ == "__main__":
#    str1 = input()
#    str2 = input()

    # 调用函数，输出结果 
    print(min_removals_to_anagram('cab', 'base') == 3)