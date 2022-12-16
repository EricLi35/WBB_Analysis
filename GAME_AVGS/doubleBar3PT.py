import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("GAME_AVGS\GameAvgAnalysis.csv")

names = data['PLAYER']
threeptt = data['3 PTT']
threeptm = data['3 PTM']

x = np.arange(len(names))
y = np.arange(threeptt.max()+1)


width = 0.4
fig, ax = plt.subplots()


rects1 = ax.bar(x-width/2 , threeptt , width, label='3 pters attempted')
rects2 = ax.bar(x+width/2 , threeptm , width, label='3 pters made' , color='#99cc00')

ax.set_ylabel('Number of Shots')
ax.set_title("Each player's 3 pt Makes and Attempts (Game Averages)")
ax.set_xticks(x, names)
ax.set_yticks(y)
ax.tick_params(axis='x', which='major', labelsize=10)
ax.legend()

# fig.tight_layout()

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light'
    )

plt.subplots_adjust(top=0.9, bottom=0.13)
plt.show()