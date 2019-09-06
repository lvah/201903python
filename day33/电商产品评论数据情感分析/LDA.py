"""

LDA 假定文档是从主题的混合生成的。这些主题又是由一些单词的特定概率分布而生成的。就像我们演练的模型一样。换句话说，LDA 假定文档以以下步骤生成：

    确定一个文档中的单词数。假设我们的文档有六个单词。
    确定该文档由哪些主题混合而来，例如，这个文档包含 1/2 的“健康”（health）主题和 1/2 的“蔬菜”（vegetables）主题。
    用每个主题的多项分布生成的单词来填充文档中的单词槽。在我们的例子中，“健康”主题占文档的 1/2，或者说占三个词。“健康”主题有“diet”这个词的可能性是 20%，或者有“execise" 这个词的概率是 15%，单词槽就是基于这些概率来填充的。

基于文档如何生成的假定，LDA 反其道而行之，并尝试找出最初哪些主题会创建这些文档。
"""


doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]



from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

raw = doc_a.lower()
tokens = tokenizer.tokenize(raw)
print(tokens)


from stop_words import get_stop_words

# create English stop words list
en_stop = get_stop_words('en')

# remove stop words from tokens
stopped_tokens = [i for i in tokens if not i in en_stop]

from nltk.stem.porter import PorterStemmer

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# stem token
texts = [p_stemmer.stem(i) for i in stopped_tokens]

print(texts)

from gensim import corpora, models

dictionary = corpora.Dictionary(texts)