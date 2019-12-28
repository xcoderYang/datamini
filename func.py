import pandas as pd
import jieba
import numpy as np
import math

#停用词集
stop = pd.read_csv('../emotion/train/stop.txt', header=0, encoding='utf-8', dtype=str, error_bad_lines=False)
stop = list(stop['keys'])

#筛选中文字符
def charDelete(uchar):
  if len(uchar)<2:
    return False
  if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
    return True
  return False

#数据分词
def tran(data, tag):
  ans = []
  data = data.astype(str)
  for i in data:
    words = " ".join(jieba.cut(i))
    words = words.split(' ')
    words = list(filter(charDelete, words))
    ans.append(words)
  if tag == True:
    return pd.Series(ans)
  else:
    return ans

def idToContain(group, contain, all):
  if len(group) == 0:
    return []

  temp_pd = pd.DataFrame()

  for key in group:
    temp_pd = pd.concat([temp_pd, all[all['id']==key][contain]], ignore_index=True)
    
  temp_pd = temp_pd[0]
  return temp_pd

#统计key出现的次数，均值，方差，和概率
def countKeys(pdCol, dataTotalCount):
  title = tran(pdCol, False)
  titleKeys = {}
  tempTitleKeys = {}
  keysCountObj = {}
  for i in range(0, len(title)):
    # 应该在这个循环里面统计
    tempTitleKeys = {}
    for j in range(0, len(title[i])):
      if title[i][j] in stop:
        continue
      if title[i][j] in titleKeys:
        titleKeys[title[i][j]] = titleKeys[title[i][j]]+1
      else:
        titleKeys[title[i][j]] = 1

      if title[i][j] in tempTitleKeys:
        tempTitleKeys[title[i][j]] = tempTitleKeys[title[i][j]]+1
      else:
        tempTitleKeys[title[i][j]] = 1
    for j in tempTitleKeys:
      if j in keysCountObj:
        keysCountObj[j].append(tempTitleKeys[j])
      else:
        keysCountObj[j]= [tempTitleKeys[j]]
  ans = []
  for i in titleKeys:
    if titleKeys[i]<2:
      continue
    allDatas = keysCountObj[i]
    sum = 0
    for count in allDatas:
      sum = count + sum
    u = sum / dataTotalCount
    sd = 0
    for count in allDatas:
      sd = sd + math.pow((count-u), 2)
    sd = math.sqrt(sd/dataTotalCount)
    ans.append({
      'key': i,
      'count': titleKeys[i],
      'u': u,
      'sd': sd
    })
  totalCount = 0
  for cur in ans:
    totalCount = totalCount + cur['count']
    cur['count']
  for i in range(0, len(ans)):
    ans[i]['radio'] = ans[i]['count']/totalCount
  ans = pd.DataFrame(ans).sort_values(by='count',ascending=False)
  return ans

#数据结构转换
def listToDict(contentWords):
  dictWords = {}
  for word in contentWords:
    if word in dictWords:
      dictWords[word] = dictWords[word]+1
    else:
      dictWords[word] = 1
  return dictWords

def completeP(x, u, sd):
  pass
  