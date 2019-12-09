import pandas as pd
import jieba
import numpy as np

data = pd.read_csv('../emotion/train/Train_DataSet.csv')
tableAns = pd.read_csv('../emotion/train/Train_DataSet_Label.csv').head(5)

tableQues = data.head(5)


#筛选中文字符
def charDelete(uchar):
  if len(uchar)<2:
    return False
  if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
    return True
  return False

ques = []
ans = []
for i in range(0, len(tableQues)):
  id = data['id'][i],
  title = list(jieba.cut(data['title'][i]))
  content = list(jieba.cut(data['content'][i]))

  title = list(filter(charDelete, title))
  content = list(filter(charDelete, content))

  ques.append({
    'id': id,
    'title': title,
    'content': content
  })

for i in range(0, len(tableAns)):
  id = tableAns['id'][i]
  label = tableAns['label'][i]

  ans.append({
    'id': id,
    'label': label
  })
positive = []
negative = []
other = []
for i in range(0, len(ans)):
  id = ans[i]['id']
  if ans[i]['label']==2:
    negative.append(id)
  elif ans[i]['label']==1:
    positive.append(id)
  else:
    other.append(id)
print(positive, negative, other)

posiKeys = []
negaKeys = []
otherKeys = []

for i in range(0, len(ques)):
  data = ques[i]
  id = data['id']
  title = data['title']
  content  = data['content']
  print(id, title, content)
  if id in positive:
    for j in range(0, len(title)):
      for index in range(0, len(posiKeys)):
        if posiKeys[index] == title[j]:
          pass
    for j in range(0, len(content)):
      pass
  elif id in negative:
    pass
  else:
    pass