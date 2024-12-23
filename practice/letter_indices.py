#编写一个程序，创建一个字典，其中给定单词的每个唯一字母表示一个键，值为字母出现的索引的列表。

#定义函数letter_indices()，参数为word(字符串)。
#在函数中，创建一个字典，其中键是单词中的唯一字母，值是包含该字母出现的索引的列表。
#返回该字典

def letter_indices(word):
    # 此处编写代码
    words_dict = dict()
    for i in range(len(word)):
        if word[i] not in words_dict:
            words_dict[word[i]] = list()
        words_dict[word[i]].append(i)
    return words_dict
        
if __name__ == "__main__":
    # 获取输入 
    #word = input()

    # 调用函数 
    print(letter_indices('pineapple') == {'p': [0, 5, 6], 'i': [1], 'n': [2], 'e': [3, 8], 'a': [4], 'l': [7]})
    print(letter_indices('banana') == {'b': [0], 'a': [1, 3, 5], 'n': [2, 4]})