import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer

# The following function would map the treebank tags 
# to WordNet part of speech names:
def get_wordnet_pos(treebank_tag):
    """
    return WORDNET POS compliance to WORDENT lemmatization (a,n,r,v) 
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ # ADJ形容词
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV  # ADV动词
    else:
        # return None
        return wordnet.NOUN


def lemmatize_sentence(tokens):
    """
    lemmatize sentence
    """
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(tokens):
        # wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        wordnet_pos = get_wordnet_pos(pos) 
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))
    return res

file_path = '/Users/hangyi/Desktop/python_work/chapter10/alice.txt'
 
with open(file_path, encoding = 'utf8') as f_obj:
    contents = f_obj.read() 

# 分词
pattern = r'[A-Za-z]+'
tokens = nltk.regexp_tokenize(contents, pattern)
# print(tokens)

# 删除停用词和长度小于3的单词
filtered_words = [w.lower() for w in tokens if w.lower() not in stopwords.words('english') and len(w)>=3]
# print(filtered_words)

# 删除标点符号
# words = [word for word in filtered_words if word.isalpha()]


# 词形归并
lemmatizered_tokens = lemmatize_sentence(filtered_words)
# print(lemmatizered_tokens)

# 统计频率
freq = nltk.FreqDist(lemmatizered_tokens)


freq.plot(10, cumulative=False)

# 将频率从大到小排列，以freq的value排序
sorted_freq = sorted(freq.items(), key=lambda d:d[1], reverse = True)
print("一共有" + str(len(sorted_freq)) + "个单词参加排序")
for key, val in sorted_freq:
    key = key.ljust(15)
    # print(str(key) + str(val))

    # 输出到文件
    filename = 'acount_result.txt'
    with open(filename, 'a',encoding = 'utf8') as f_obj:
        f_obj.write(key + " " + str(val) + "\n")

