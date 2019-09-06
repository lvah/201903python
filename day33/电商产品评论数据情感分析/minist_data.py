# -*- coding: utf-8 -*-
import pandas as pd
"""
Gensim是一款开源的第三方Python工具包，用于从原始的非结构化的文本中，无监督地学习到文本隐层的主题向量表达。
它支持包括TF-IDF，LSA，LDA，和word2vec在内的多种主题模型算法，支持流式训练，并提供了诸如相似度计算，信息
检索等一些常用任务的API接口。


# 1. LDA 是什么？
隐含狄利克雷分布（以下简写为 LDA）是一种主题模型，它基于一组文档中的词频生成主题。对于在给定的文档集中准确合理地找到主题的混合，LDA 是一种非常有效的方法。

LDA 假定文档是从主题的混合生成的。这些主题又是由一些单词的特定概率分布而生成的。就像我们演练的模型一样。换句话说，LDA 假定文档以以下步骤生成：

    确定一个文档中的单词数。假设我们的文档有六个单词。 
    确定该文档由哪些主题混合而来，例如，这个文档包含 1/2 的“健康”（health）主题和 1/2 的“蔬菜”（vegetables）主题。
    用每个主题的多项分布生成的单词来填充文档中的单词槽。在我们的例子中，“健康”主题占文档的 1/2，或者说占三个词。“健康”主题有“diet”这个词的可能性是 20%，或者有“execise" 这个词的概率是 15%，单词槽就是基于这些概率来填充的。

基于文档如何生成的假定，LDA 反其道而行之，并尝试找出最初哪些主题会创建这些文档。

"""
from gensim import corpora, models

def LDA():
    '''
    LDA主题分析
    :return:
    '''
    # 参数初始化
    negfile = 'data/output/meidi_jd_neg_cut.txt'
    posfile = 'data/output/meidi_jd_pos_cut.txt'
    stoplist = 'data/stoplist.txt'

    neg = pd.read_csv(negfile, encoding='utf-8', header=None)  # 读入数据
    pos = pd.read_csv(posfile, encoding='utf-8', header=None)
    stop = pd.read_csv(stoplist, encoding='utf-8', header=None, sep='tipdm', engine='python')
    # sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错
    # 所以解决办法是手动设置一个不存在的分割词，如tipdm。

    # Pandas自动过滤了空格符，这里手动添加
    stop = [' ', ''] + list(stop[0])

    # 定义一个分割函数，然后用apply广播, 去除停用词
    """
    neg: 
                                                           0
            0  好像 遥控 是 坏 的   还是 送 的 电池 没有 电   算了   热水器 上将 就 着...
            1                         要 打 十个 字 才能 发   我 就 打 十个 字
            2  调温 的 开关 太紧 了   不 知道 是不是 都 这样   送货 和 安装 的 师傅 来 ...
            3           上面 安装 既然 花 了 我 差不多 * 块   但是 这 热水器 马马虎虎 吧
            4             这 东西 有 不是 什么 高科技   比 别的 厂家 还贵   想 不 明白
    
    """
    neg[1] = neg[0].apply(lambda s: s.split(' '))  # ["好像", "遥控", "电池"， “的”]
    neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop])  # # ["好像", "遥控", "电池"] 去掉了停用词
    pos[1] = pos[0].apply(lambda s: s.split(' '))
    pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stop])

    # ***************************************负面主题分析***********************************
    # 调用Gensim提供的API建立语料特征（此处即是word）的索引字典; 构建字典8038条, neg_dict=[xx, xx, xx]
    neg_dict = corpora.Dictionary(neg[2])
    # 建立语料库，
    """
    # 代表字典中的第0个索引词出现了1次， 第1个索引词出现了1次，
    [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
    #  代表字典中的第9个索引词出现了2次，
    [(9, 2), (10, 1), (11, 2)]
    [(12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1)]
    [(3, 1), (16, 1), (24, 1), (25, 1), (26, 1), (27, 1)]
    [(28, 1), (29, 1), (30, 1), (31, 1), (32, 1), (33, 1)]
    """
    neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]]


    """
    corpus: 必须。语料库
    num_topics: 必须。LDA 模型要求用户决定应该生成多少个主题。由于我们的文档集很小，所以我们只生成三个主题;
    id2word：必须。LdaModel 类要求我们之前的 dictionary 把 id 都映射成为字符串;
    passes：可选。模型遍历语料库的次数。遍历的次数越多，模型越精确。

    """
    # LDA模型训练
    neg_lda = models.LdaModel(neg_corpus, num_topics=3, id2word=neg_dict)
    for i in range(3):
        result = neg_lda.print_topic(i)  # 输出每个主题(聚类结果的输出)
        print("差评: ", result)

    # ***************************************正面主题分析***********************************
    pos_dict = corpora.Dictionary(pos[2])
    pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
    pos_lda = models.LdaModel(pos_corpus, num_topics=3, id2word=pos_dict)
    for i in range(3):
        neg_lda.print_topic(i)  # 输出每个主题
        print("好评: ", pos_lda.print_topic(i))


if __name__ == '__main__':
    LDA()