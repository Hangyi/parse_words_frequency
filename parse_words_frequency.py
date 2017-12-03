"""
    还要不完善的地方
    1. ’s, 've, 're, 没有删去
    2. 有些数字，乱入
    3. 一个单词的时态变化重复计数
    4. 程序不够模块化
    5. 白名单功能，根据柯林斯词频分级,设置筛选粒度
    6. 自动加上中文意思
"""
file_path = '/Users/hangyi/Desktop/python_work/chapter10/little_women.txt'

try:    
    with open(file_path, encoding = 'utf8') as f_obj:
        contents = f_obj.read().lower()                                                                                         
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 去掉字符串里的标点符号   
    remap = {
        ord(',') : None,
        ord('.') : None,
        ord('?') : None,
        ord('!') : None,
        ord('(') : None,
        ord(')') : None,
        ord('[') : None,
        ord(']') : None,
        ord('{') : None,
        ord('}') : None,
        ord('*') : None,
        ord(';') : None,
        ord(':') : None,
        ord('"') : None,
        ord('#') : None,
        ord('0') : ' ',
        ord('1') : ' ',
        ord('2') : ' ',
        ord('3') : ' ',
        ord('4') : ' ',
        ord('5') : ' ',
        ord('6') : ' ',
        ord('7') : ' ',
        ord('8') : ' ',
        ord('9') : ' ',
        ord('-') : ' ',
        ord('\'') : ' ',
        ord('/') : ' ',
    }

    # text = contents.translate(remap)
    # 将字符串转化为单词列表
    no_punctuation_countents = contents.translate(remap)
    words = no_punctuation_countents.split()
    # print(words)

    # 先把列表里的单词全部转化为小写
    # lower_words = []
    # for word in words:
    #     # print(word)
    #     lower_words.append(word.lower())

    # print(lower_words)
    
    # 获得去重后的单词列表
    unique_words = list(set(words))

    # 统计有多少不重复的单词
    num_unique_words = len(unique_words)
    print(num_unique_words)
    # print(unique_words)
    
    #遍历列表，统计每个单词出现的数量
    word_result = {}
    for word in unique_words:
        times = no_punctuation_countents.count(word)
        word_result[word] = times
    # print(word_result)

    # 按顺序排列
    sorted_word_result = sorted(word_result.items(), key=lambda items:items[1], reverse = True)
    for word, times in sorted_word_result:
        word = word.ljust(15)
        # print(word + " " + str(times))
    
        # 输出到文件
        filename = 'acount_result.txt'
        with open(filename, 'a',encoding = 'utf8') as f_obj:
            f_obj.write(word + " " + str(times) + "\n")
