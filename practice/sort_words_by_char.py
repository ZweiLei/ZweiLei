def sort_words_by_char(words: list, index: int) -> list:
    # 在此处编写代码
#    words.sort(key=lambda word:word[index - 1])
    return sorted(words, key=lambda word:word[index - 1])

if __name__ == "__main__":
    # 获取用户输入
    #words = input().split() # 单词列表
    #index = int(input())    # 位置

    # 调用函数
    print(sort_words_by_char(['helium', 'oxygen', 'nitrogen'], 4) == ['oxygen', 'helium', 'nitrogen'])