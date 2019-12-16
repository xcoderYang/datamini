import pandas as pd
import jieba
import numpy as np

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

def tranStr(str):
  words = " ".join(jieba.cut(str))
  words = words.split(' ')
  words = list(filter(charDelete, words))
  return words

def idToContain(group, contain, all):
  if len(group) == 0:
    return []

  temp_pd = pd.DataFrame()

  for key in group:
    temp_pd = pd.concat([temp_pd, all[all['id']==key][contain]], ignore_index=True)
    
  temp_pd = temp_pd[0]
  return temp_pd

def countKeys(pdCol):
  title = tran(pdCol, False)
  titleKeys = {}
  for i in range(0, len(title)):
    for j in range(0, len(title[i])):
      if title[i][j] in stop:
        continue
      if title[i][j] in titleKeys:
        titleKeys[title[i][j]] = titleKeys[title[i][j]]+1
      else:
        titleKeys[title[i][j]] = 1
  ans = []
  for i in titleKeys:
    if titleKeys[i]<10:
      continue
    ans.append({
      'key': i,
      'count': titleKeys[i]
    })
  ans = pd.DataFrame(ans).sort_values(by='count',ascending=False)
  return ans

def listToDict(contentWords):
  dictWords = {}
  for word in contentWords:
    if word in dictWords:
      dictWords[word] = dictWords[word]+1
    else:
      dictWords[word] = 1
  return dictWords