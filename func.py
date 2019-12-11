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