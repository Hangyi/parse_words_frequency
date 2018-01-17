import re

file_path = '/Users/hangyi/Desktop/python_work/chapter10/alice.txt'
 
try:
    with open(file_path, encoding = 'utf8') as f_obj:
        contents = f_obj.read()                                                                                    
except FileNotFoundError:
    msg = "Sorry, the file " + file_path + " does not exist."
    print(msg)
else:
    # 使用正则
    clean_contents = re.sub('[\t\n]+', " ", contents) # 删除制表符和换行符
    clean_contents = re.sub("[^A-Za-z\s]", " ", contents) 


    words = clean_contents.split()
    # print(words)
    
    # 获得去重后的单词列表
    unique_words = list(set(words))
    
    # coca前150单词
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", 
        "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
        "they", "is", "an", "at", "but","we", "his", "from", "that", "not", 
        "by", "she", "or", "as", "what", "go", "their","can", "who", "get", 
        "if", "would", "her", "all", "my", "make", "about", "know", "will", 
        "as", "up", "one", "time", "has", "been", "there", "year", "so", 
        "think", "when", "which", "them", "some", "me", "people", "take", 
        "out", "into", "just", "see", "him", "your", "come", "could", "now", 
        "than", "like", "other", "how", "then", "its", "our", "two", "more", 
        "these", "want", "way", "look", "first", "also", "new", "because", 
        "day", "more", "use", "no", "man", "find", "here", "thing", "give", 
        "many", "well", "only", "those", "tell", "one", "very", "her", 
        "even", "back", "any", "good", "woman", "through", "us", "life",
        "child", "there", "work", "down", "may", "after", "should", "call",
        "world", "over", "school", "still", "try", "in", "as", "last", 
        "ask", "need", "too", "fell", "three", "when", "state", "never",
        "become", "between", "high", "really", "something", "most", "another",
        "much", "family", "own", "out", "leave"] 

    # 删掉长度<3的单词和处于commonWords里的单词
    for word in unique_words[0:]:
        if len(word) < 3 or word in commonWords:
            unique_words.remove(word)

    # print(unique_words)

    # 统计有多少不重复的单词
    num_unique_words = len(unique_words)
    print(num_unique_words)
    # print(unique_words)
    
    #遍历列表，统计每个单词出现的数量
    word_result = {}
    for word in unique_words:
        times = clean_contents.count(word)
        word_result[word] = times
    # print(word_result)

    # 按顺序排列
    sorted_word_result = sorted(word_result.items(), key=lambda items:items[1], reverse = True)
    for word, times in sorted_word_result:
        word = word.ljust(15)
        # print(word + " " +- str(times))                
    
        # 输出到文件
        filename = 'acount_result4.txt'
        with open(filename, 'a',encoding = 'utf8') as f_obj:
            f_obj.write(word + " " + str(times) + "\n")
