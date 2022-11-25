#Datafr object accept data frame as paramerer
#df for dataframe, av for number of col average
class Datafr:
    def __init__(self,df):
        self.dataframe=df
        
    def dataframeavg(self,av,date='timestamp',status='SystemStatus',fail='System Down'):
        row,col=(self.dataframe.shape)
        di={}
        li=[]
        for i in self.dataframe.columns:
            di[i]=[]
            li.append(i)
        c=0
        for i in range(row):
            if c!=av-1:
                try:
                    if self.dataframe[status][i]!=self.dataframe[status][i+1]:
                        if c!=0:
                            n=0
                            for j in li:
                                if j==date or j==status:
                                    di[j].append(self.dataframe.loc[i-c][n])
                                else:
                                    di[j].append(self.dataframe[j][i-c:i+1].mean())
                                n+=1
                            
                        else:
                           
                            n=0
                            for j in li:
                                di[j].append(self.dataframe.loc[i][n])
                                n+=1
                        c=-1
                except:
                    print(c,i,row)
                    c+=1
                    if c>0:
                        n=0
                        for j in li:
                            if j==date or j==status:
                                di[j].append(self.dataframe.loc[row-c][n])
                            else:
                                di[j].append(self.dataframe[j][row-c:].mean())
                            n+=1
                    else:  
                        n=0
                        for j in li:
                            di[j].append(self.dataframe.loc[i][n])
                            n+=1
            if c==av-1:
                n=0
                for j in li:
                    if j==date or j==status:
                        di[j].append(self.dataframe.loc[i-c][n])
                    else:
                        di[j].append(self.dataframe[j][i-c:i+1].mean())
                    n+=1
                c=-1
            c+=1
        return di