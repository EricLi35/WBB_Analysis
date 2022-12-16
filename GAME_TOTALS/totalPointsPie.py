import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')
pts = []
names = []


for i in range(len(data['PLAYER'])):
    if(data['PTS'][i] != 0):
        print(data['PLAYER'][i]," got 0 points")
        names.append(data['PLAYER'][i])
        pts.append(data['PTS'][i])

explode=(0,0,0.2,0.2,0,0,0.2,0.2,0,0,0,0,0,0)

fig,ax = plt.subplots()
ax.pie(pts , labels=names , explode=explode,textprops={'fontsize': 8.5})
ax.axis('equal')

ax.set_title("Allocation of Points Scored, out of "+str(data['PTS'].sum())+ " Combined Points")
# fig.tight_layout()

plt.show()