# -*- coding: UTF-8 -*-

import pandas as pd
import jieba
import numpy as np
from func import tran, idToContain, countKeys, charDelete, listToDict
import math
# #训练集数据
# tableQues = pd.read_csv('../emotion/train/Train_DataSet.csv', header=0, encoding='utf-8', dtype=str)

# # 训练集答案
# tableAns = pd.read_csv('../emotion/train/Train_DataSet_Label.csv', header=0, encoding='utf-8', dtype=str)

# testDataSet = pd.read_csv('../emotion/test/Test_DataSet.csv', header=0, encoding='utf-8', dtype=str)

# #本地测试，取前5条数据
# testQues = tableQues
# testAns = tableAns

# positive = []
# positiveKeys = []

# negative = []
# negativeKeys = []

# other = []
# otherKeys = []

# positive = list(testAns[testAns['label']=='1']['id'])

# negative = list(testAns[testAns['label']=='2']['id'])

# other = list(testAns[testAns['label']=='0']['id'])

# positiveContentPd = idToContain(positive, 'content', testQues)
# negativeContentPd = idToContain(negative, 'content', testQues)
# otherContentPd = idToContain(other, 'content', testQues)


# posiTotalCount = tableAns[tableAns['label']=='1'].shape[0]
# negaTotalCount = tableAns[tableAns['label']=='2'].shape[0]
# otherTotalCount = tableAns[tableAns['label']=='0'].shape[0]

# title = testQues['title']

# positiveKeys = countKeys(positiveContentPd, posiTotalCount)
# negativeKeys = countKeys(negativeContentPd, negaTotalCount)
# otherKeys = countKeys(otherContentPd, otherTotalCount)

# positiveKeys.to_csv('./positiveContentKeys.csv', sep=',', header=True, index=True)
# negativeKeys.to_csv('./negativeContentKeys.csv', sep=',', header=True, index=True)
# otherKeys.to_csv('./otherContentKeys.csv', sep=',', header=True, index=True)

# print('写入成功, 开始处理')
# input()

otherTitleKey = pd.read_csv('./positiveContentKeys.csv', header=0, encoding='utf-8', dtype=str).head(50)
posiTitleKey = pd.read_csv('./otherContentKeys.csv', header=0, encoding='utf-8', dtype=str).head(50)
negaTitleKey = pd.read_csv('./negativeContentKeys.csv', header=0, encoding='utf-8', dtype=str).head(50)
testDataSet = pd.read_csv('./Test_DataSet.csv', header=0, encoding='utf-8', dtype=str)

tableAns = pd.read_csv('../emotion/train/Train_DataSet_Label.csv', header=0, encoding='utf-8', dtype=str)

posiTotalCount = tableAns[tableAns['label']=='1'].shape[0]
negaTotalCount = tableAns[tableAns['label']=='2'].shape[0]
otherTotalCount = tableAns[tableAns['label']=='0'].shape[0]

print(posiTotalCount, negaTotalCount, otherTotalCount)

testDataAns = []
datas = testDataSet.values

posiKeyGroup = list(posiTitleKey['key'])
negaKeyGroup = list(negaTitleKey['key'])
otherKeyGroup = list(otherTitleKey['key'])


for data in datas:
  No = data[0]
  title = data[1]
  content = data[2]
  posiRate = 1
  negaRate = 1
  otherRate = 1
  # titleWords = " ".join(jieba.cut(title)).split(" ")
  # titleWords = list(filter(charDelete, titleWords))
  contentWords = " ".join(jieba.cut(content)).split(" ")
  contentWords = list(filter(charDelete, contentWords))
  contentWords = listToDict(contentWords)
  contentWords = sorted(contentWords.items(), key = lambda item:item[1], reverse = True)
  contentWords = list(filter(lambda item: item[1]>1, contentWords))
  
  #percent
  for group in contentWords:
    if group[0] in otherKeyGroup:
      u = float(list(otherTitleKey[otherTitleKey['key']==group[0]]['u'])[0])
      sd = float(list(otherTitleKey[otherTitleKey['key']==group[0]]['sd'])[0])
      # 前面还有 1/math.sqrt(2*Π),常数，故省略
      otherRate = otherRate * (1/sd*math.exp(-math.pow((group[1]-u),2)/(2*math.pow(sd, 2))))
    else:
      otherRate = otherRate*0.01
    
    if group[0] in posiKeyGroup:
      u = float(list(posiTitleKey[posiTitleKey['key']==group[0]]['u'])[0])
      sd = float(list(posiTitleKey[posiTitleKey['key']==group[0]]['sd'])[0])
      posiRate = posiRate * (1/sd*math.exp(-math.pow((group[1]-u),2)/(2*math.pow(sd, 2))))
    else:
      posiRate = posiRate*0.01

    if group[0] in negaKeyGroup:
      u = float(list(negaTitleKey[negaTitleKey['key']==group[0]]['u'])[0])
      sd = float(list(negaTitleKey[negaTitleKey['key']==group[0]]['sd'])[0])
      negaRate = negaRate * (1/sd*math.exp(-math.pow((group[1]-u),2)/(2*math.pow(sd, 2))))
    else:
      negaRate = negaRate*0.01

  print(content)
  print(posiRate, negaRate, otherRate)
  input()
    
  #testDataAns
  
  
