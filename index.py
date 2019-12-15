# -*- coding: UTF-8 -*-

import pandas as pd
import jieba
import numpy as np
from func import tran, keysIn, tranStr, idToContain, countKeys

# 测试集数据
tableQues = pd.read_csv('../emotion/train/Train_DataSet.csv', header=0, encoding='utf-8', dtype=str)

# 测试集答案
tableAns = pd.read_csv('../emotion/train/Train_DataSet_Label.csv', header=0, encoding='utf-8', dtype=str)

stop = pd.read_csv('../emotion/train/stop_utf8.xlsx', header=0, encoding='utf-8', dtype=str, error_bad_lines=False)

print(stop)

input()
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

print(positiveTitlePd)
print(negativeTitlePd)
print(otherTitlePd)

# positive = list(test)
#title计数
title = testQues['title']
positiveKeys = countKeys(positiveTitlePd)
negativeKeys = countKeys(negativeTitlePd)
otherKeys = countKeys(otherTitlePd)



positiveKeys.to_csv('./positiveKeys.csv', sep=',', header=True, index=True)
negativeKeys.to_csv('./negativeKeys.csv', sep=',', header=True, index=True)
otherKeys.to_csv('./otherKeys.csv', sep=',', header=True, index=True)
print('success Input')

# title = tran(negativeTitlePd, False)
# titleKeys = []
# for i in range(0, len(title)):
#   for j in range(0, len(title[i])):
#     titleKeys = keysIn(title[i][j], titleKeys)
# pdTitle = pd.DataFrame(titleKeys).sort_values(by='count',ascending=False)
# print(pdTitle)

# #content计数
# content = testQues['content']
# content = tran(content, False)
# contentKeys = []
# for i in range(0, len(content)):
#   for j in range(0, len(content[i])):
#     contentKeys = keysIn(content[i][j], contentKeys)
# pdContent = pd.DataFrame(contentKeys).sort_values(by='count',ascending=False)
# print(pdContent)

# #pandas数据库    
# testQues = testQues.assign(splitTitle = lambda x: tran(x['title'], True))
# test = testQues.assign(splitContent = lambda x: tran(x['content'], True))
# print(test['splitTitle'])
# print(test['splitContent'])