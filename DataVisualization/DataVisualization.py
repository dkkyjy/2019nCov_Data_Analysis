import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataFile = '2019nCov.xlsx'
df = pd.read_excel(dataFile).T[1:]
print(df.dtypes)
print(df.index)
print(df.columns)

date = pd.to_datetime(df.index.astype('str').values)
df.index = date

#新增确诊
quezhenNewTotal = df[2]
quezhenNewHubei = df[3]
quezhenNewOther = df[4]
plt.figure()
quezhenNewOther.plot()
plt.savefig('quezhenNewOther.png')

#新增重症
zhongzhengNewTotal = df[6]
zhongzhengNewHubei = df[7]
zhongzhengNewOther = df[8]

#新增死亡
siwangNewTotal = df[10]
siwangNewHubei = df[11]
siwangNewOther = df[12]
plt.figure()
siwangNewOther.plot()
plt.savefig('siwangNewOther.png')

#新增治愈
zhiyuNewTotal = df[14]
zhiyuNewHubei = df[15]
zhiyuNewOther = df[16]
plt.figure()
zhiyuNewOther.plot()
plt.savefig('zhiyuNewOther.png')

#新增疑似
yisiNewTotal = df[18]
yisiNewHubei = df[19]
yisiNewOther = df[20]

#累计确诊
quezhenSumTotal = df[23]
quezhenSumHubei = df[24]
quezhenSumOther = df[25]
plt.figure()
quezhenSumOther.plot()
plt.savefig('quezhenSumOther.png')

#累计重症
zhongzhengSumTotal = df[27]
zhongzhengSumHubei = df[28]
zhongzhengSumOther = df[29]

#累计死亡
siwangSumTotal = df[31]
siwangSumHubei = df[32]
siwangSumOther = df[33]
plt.figure()
siwangSumOther.plot()
plt.savefig('siwangSumOther.png')

#累计治愈
zhiyuSumTotal = df[35]
zhiyuSumHubei = df[36]
zhiyuSumOther = df[37]
plt.figure()
zhiyuSumOther.plot()
plt.savefig('zhiyuSumOther.png')

#累计疑似
yisiSumTotal = df[39]
yisiSumHubei = df[40]
yisiSumOther = df[41]