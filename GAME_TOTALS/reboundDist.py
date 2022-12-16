import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')

oreb = data['OR']
dreb = data['DR']
names = data['PLAYER']

x = np.arange(len(names))
y = np.arange(0,50,5)

width = 0.35
fig,ax = plt.subplots()
rects1 = ax.bar(x-width/2 , dreb , width, label='Defensive Rebounds')
rects2 = ax.bar(x+width/2 , oreb , width, label='Offensive Rebounds')

ax.set_ylabel("Number of Rebounds")
ax.set_title("Each Player's Offensive & Defensive Rebounds (Game Totals)")

ax.set_xticks(x,names)
ax.set_yticks(y)

ax.legend()

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light'
    )

print(oreb.head(5))
print(dreb.head(5))

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.13)
ax.bar_label(rects1,padding=2,size=8.5)
ax.bar_label(rects2,padding=2,size=8.5)
plt.show()

