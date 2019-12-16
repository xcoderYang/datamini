# -*- coding: UTF-8 -*-

import pandas as pd
import jieba
import numpy as np
from func import tran, idToContain, countKeys, charDelete, listToDict
# 训练集数据
tableQues = pd.read_csv('../emotion/train/Train_DataSet.csv', header=0, encoding='utf-8', dtype=str)

# 训练集答案
tableAns = pd.read_csv('../emotion/train/Train_DataSet_Label.csv', header=0, encoding='utf-8', dtype=str)

testDataSet = pd.read_csv('../emotion/test/Test_DataSet.csv', header=0, encoding='utf-8', dtype=str)
#see
# see = pd.read_csv('./positiveContentKeys.csv', header=0, encoding='utf-8', dtype=str)
# print(see)

#本地测试，取前5条数据
testQues = tableQues
testAns = tableAns

positive = []
positiveKeys = []

negative = []
negativeKeys = []

other = []
otherKeys = []

positive = list(testAns[testAns['label']=='1']['id'])

negative = list(testAns[testAns['label']=='2']['id'])

other = list(testAns[testAns['label']=='0']['id'])


positiveTitlePd = idToContain(positive, 'title', testQues)
negativeTitlePd = idToContain(negative, 'title', testQues)
otherTitlePd = idToContain(other, 'title', testQues)

positiveContentPd = idToContain(positive, 'content', testQues)
negativeContentPd = idToContain(negative, 'content', testQues)
otherContentPd = idToContain(other, 'content', testQues)

# print(positiveTitlePd)
# print(negativeTitlePd)
# print(otherTitlePd)

# positive = list(test)
#title计数
title = testQues['title']

#print(positiveContentPd)
positiveKeys = countKeys(positiveContentPd)
negativeKeys = countKeys(negativeContentPd)
otherKeys = countKeys(otherContentPd)

positiveKeys.to_csv('./positiveContentKeys.csv', sep=',', header=True, index=True)
negativeKeys.to_csv('./negativeContentKeys.csv', sep=',', header=True, index=True)
otherKeys.to_csv('./otherContentKeys.csv', sep=',', header=True, index=True)
#print('success content')

positiveKeys = countKeys(positiveTitlePd)
negativeKeys = countKeys(negativeTitlePd)
otherKeys = countKeys(otherTitlePd)

positiveKeys.to_csv('./positiveContentKeys.csv', sep=',', header=True, index=True)
negativeKeys.to_csv('./negativeContentKeys.csv', sep=',', header=True, index=True)
otherKeys.to_csv('./otherContentKeys.csv', sep=',', header=True, index=True)


# testDataAns = []
# datas = testDataSet.values


# for data in datas:
#   No = data[0]
#   title = data[1]
#   content = data[2]
#   titleWords = " ".join(jieba.cut(title)).split(" ")
#   titleWords = list(filter(charDelete, titleWords))
#   contentWords = " ".join(jieba.cut(content)).split(" ")
#   contentWords = list(filter(charDelete, contentWords))
#   dictWords = listToDict(contentWords)
#   dictWords = sorted(dictWords.items(), key = lambda item:item[1], reverse = True)
#   dictWords = list(filter(lambda item: item[1]>1, dictWords))
#   print(dictWords)
#   input()
  
