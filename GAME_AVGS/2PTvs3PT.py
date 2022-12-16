import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("GAME_AVGS\GameAvgAnalysis.csv")

names = data['PLAYER']
two = data['2 PT%']
three = data['3 PT%']

finaltwo = [float(num[0:len(num)-1]) for num in two]
finalthree = [float(num[0:len(num)-1]) for num in three]

x = np.linspace(start=0,stop=100,num=21)
y = np.arange(len(names))
width = 0.3

fig, ax = plt.subplots()
rects1 = ax.barh(y-width/2 , finaltwo , width, label='2 pt FG%')
rects2 = ax.barh(y+width/2 , finalthree , width, label='3 pt FG%' , color='#99cc00')

ax.set_yticks(y, names)
ax.set_xticks(x)

ax.bar_label(rects1,padding=2,size=8.5)
ax.bar_label(rects2,padding=2,size=8.5)

ax.set_xlabel("Field Goal Percentage")
ax.set_title("Each Player's 2pt FG% and 3pt FG% (Across Game Averages)")

ax.legend()

plt.show()
