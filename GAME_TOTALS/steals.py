import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')
names = data['PLAYER']
steals = data['STEALS']

fig,ax = plt.subplots()

x = np.arange(len(names))
width = 0.35

rects1 = ax.bar(x , steals , width)

ax.set_xticks(x,names)

plt.xticks(rotation=45)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.13)

ax.bar_label(rects1,padding=2,size=8.5)

plt.show()