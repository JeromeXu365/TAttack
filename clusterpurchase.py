import pandas as pd
import time
import numpy as np
from reader_pandas import reader_pandas


user= pd.read_csv('D://PurchaseDataset//transactions.csv', chunksize=3500000)
count = 0
df2 = pd.DataFrame({})
t0 = time.time()
t2 = t0
for df in user:
    count += 1
    t1 = time.time()
    print('Finish {}%'.format(count))
    print('\n 用时%.2f seconds' % (t1 - t2))
    #print(count)
    #print(df.head(5))
    df2 = df[['id']]
    df2 = df2.sort_values('id', ascending=True)
    df2 = df2.drop_duplicates(['id'])
    df2.to_csv('D://PurchaseDataset//idlist.csv', sep=',',mode='a',header=False)
    t2 = time.time()

'''
reader=pd.read_csv('D://PurchaseDataset//transactions.csv', iterator=True)#分块读取
chunkSize = 10000000 #一次读取一千万条记录
chunks = []
chunk = reader.get_chunk(chunkSize) #一次获得1kw的数据量
chunks.append(chunk)
df = pd.concat(chunks, ignore_index=True)
#读取完数据后再利用pandas的concate连接DataFrame
'''


#df2 = df2.transpose()


'''
reader=pd.read_csv('D://PurchaseDataset//namelist.csv', iterator=True)#分块读取
chunkSize = 10 #一次读取10条记录
chunks = []
chunk = reader.get_chunk(chunkSize) #一次获得10的数据量
chunks.append(chunk)
df1 = pd.concat(chunks, ignore_index=True)
#读取完数据后再利用pandas的concate连接DataFrame
'''

'''
df2 = df[['id','category']]
print(df.columns)
print(df1.columns)
print(df2.head(5))

for i in range(chunkSize):
    print(df2.iat[i,0],df2.iat[i,1])
'''

'''
df1 = df[['id','category']]
df2 = df[['category']]

df2 = df2.sort_values('category',ascending=True)
df2 = df2.drop_duplicates(['category'])
df2 = df2.transpose()
df2.to_csv('D://PurchaseDataset//namelist.csv',sep=',')
# 把找出来的产品名称保存
'''





