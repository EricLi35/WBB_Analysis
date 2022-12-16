import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')
assists = []
names = []
colours={'#1 Kate J.':'C0','#2 Azalya F.':'C1','#5 Hailey C.':'C2','#6 Katie H.':'C3',
'#8 Sara T.':'C4','#9 Olivia W.':'C5','#10 Ryann K.':'C6','#12 Dina S.':'C7','#13 Olivia M.':'C8',
'#15 Emily M.':'C9','#21 Teigan M.':'C1'}

for i in range(len(data['PLAYER'])):
    if(data['ASSISTS'][i] != 0):
        names.append(data['PLAYER'][i])
        assists.append(data['ASSISTS'][i])
    else:
        print(data['PLAYER'][i]," got 0 assists")


fig,ax = plt.subplots()
ax.pie(assists , labels=names , textprops={'fontsize': 8.5}, autopct='%1.1f%%' , colors=[colours[key] for key in names])
ax.axis('equal')

ax.set_title("Allocation of Assists, out of "+str(data['ASSISTS'].sum())+ " Combined Assists (Game Totals)")
# fig.tight_layout()

plt.show()