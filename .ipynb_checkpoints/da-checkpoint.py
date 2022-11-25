import pandas as pd
df=pd.read_csv("./Book1.csv")
print((df['MTH_MIL_IML1_SYSFAN_VIB_VI_A'][0:10].mean()))
row,col=(df.shape)
sf=df.loc[1][1]
# print(sf)
di={}
li=[]
for i in df.columns:
    di[i]=[]
    li.append(i)
# print(di)
c=0
for i in range(row):
    if df['SystemStatus'][i]=='Failed':
        n=0
        for j in li:
            if j=='timestam' or j=='SystemStatus':
                di[j].append(df.loc[i][n])
            else:
                di[j].append(df[j][i-c:i])
            di[j].append(df.loc[i][n])
            n+=1
        c=0
    if(c==10):
        n=0
        for j in li:
            if j=='timestam' or j=='SystemStatus':
                di[j].append(df.loc[i][n])
            else:
                di[j].append(df[j][i-c:i])
            n+=1
        c=-1
    c+=1
ss=pd.DataFrame(di)
print(ss)