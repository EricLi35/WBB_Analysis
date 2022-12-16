import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("GAME_AVGS\GameAvgAnalysis.csv")

names = data['PLAYER']
twoptt = data['2 PTT']
twoptm = data['2 PTM']

x = np.arange(len(names))
y = np.arange(twoptt.max()+1)

width = 0.3
fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2 , twoptt , width, label='2 pters attempted')
rects2 = ax.bar(x+width/2 , twoptm , width, label='2 pters made' , color='#99cc00')

ax.set_ylabel('Number of Shots')
ax.set_title("Each player's 2 pt Makes and Attempted (Game Averages)")

# Axes.set_xticks(ticks, labels=None) where ticks is list of tick locations (floats)
# and labels (optional) is a list of strings that labels the ticks 
ax.set_xticks(x, names)
ax.set_yticks(y)

# change the font size of the labels (in this case, x-axis and only the major ticks)
ax.tick_params(axis='x', which='major', labelsize=9.5)

ax.legend()

# remove whitespace (found that it didn't seem to help, only worsened matters)
# fig.tight_layout()

# adjust rotation and boldness of (in this case, x-axis)
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light'
    )

# phyiscally change the dimensions of the plot when outputted 
# (takes in values as the actual position (imagine a coordinate grid))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.13)
plt.show()