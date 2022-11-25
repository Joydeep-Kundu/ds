#Datafr object accept data frame as paramerer
#df for dataframe, av for number of col average
class Datafr:
    def __init__(self,df):
        self.dataframe=df
        
    def dataframeavg(self,av,date='timestamp',status='SystemStatus',fail='Failed'):
        row,col=(self.dataframe.shape)
        di={}
        li=[]
        for i in self.dataframe.columns:
            di[i]=[]
            li.append(i)
        c=0
        for i in range(row):
            if self.dataframe[status][i]==fail:
                n=0
                for j in li:
                    if j==date or j==status:
                        di[j].append(self.dataframe.loc[i-c][n])
                    else:
                        di[j].append(self.dataframe[j][i-c:i].mean())
                    di[j].append(self.dataframe.loc[i][n])
                    n+=1
                c=-1
            if(c==av):
                n=0
                for j in li:
                    if j==date or j==status:
                        di[j].append(self.dataframe.loc[i-c][n])
                    else:
                        di[j].append(self.dataframe[j][i-c:i].mean())
                    n+=1
                c=-1
            c+=1
        if self.dataframe[status][row-1]!=fail:
            try:
                n=0
                for j in li:
                    if j==date or j==status:
                        di[j].append(self.dataframe.loc[i-c+1][n])
                    else:
                        di[j].append(self.dataframe[j][i-c+1:].mean())
                    n+=1
            except:
                n=0
                for j in li:
                    if j==date or j==status:
                        di[j].append(self.dataframe.loc[i-c][n])
                    else:
                        di[j].append(self.dataframe[j][i-c+1:].mean())
                    n+=1
        return di