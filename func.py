import pandas as pd
import jieba
import numpy as np

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

#arr = [{key:<str>, count:<num>}]
#检测 arr中是否存在 key
def keysIn(key, arr):
  for i in range(0, len(arr)):
    if(arr[i]['key'] == key):
      arr[i]['count'] = arr[i]['count']+1
      break
  else:
    arr.append({
      'key': key,
      'count': 1
    })
  return arr

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
  titleKeys = []
  for i in range(0, len(title)):
    for j in range(0, len(title[i])):
      titleKeys = keysIn(title[i][j], titleKeys)
  ans = pd.DataFrame(titleKeys).sort_values(by='count',ascending=False)
  return ans