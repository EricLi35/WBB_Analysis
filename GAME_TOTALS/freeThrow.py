import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')

names = data['PLAYER']
ftm = data['FTM']
ftt = data['FTT']


x = np.arange(len(names))
y = np.arange(0,55,5)

width = 0.35
fig,ax = plt.subplots()
rects1 = ax.bar(x-width/2 , ftm , width , label='Free Throws Attempted')
rects2 = ax.bar(x+width/2 , ftt , width , label='Free Throws Made')

ax.set_yticks(y)
ax.set_xticks(x, names)

plt.xticks(rotation=45 , fontweight='light')

ax.legend()

ax.set_ylabel("Number of Free Throws")
ax.set_title("Player's Free Throws Attempts and Makes (Game Totals)")

ax.bar_label(rects1, padding=2 , size=8.5)
ax.bar_label(rects2, padding=2 , size=8.5)

plt.subplots_adjust(left=0.1 , right=0.9 , top=0.9 , bottom=0.13)
plt.show()
