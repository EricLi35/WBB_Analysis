import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')
to = data['TO']
played = data['Played']
names = data['PLAYER']

print(to.head(3))
print(played.head(3))

x = np.arange(len(names))
y = np.arange(0,45,5)

width = 0.35
fig,ax = plt.subplots()
rects1 = ax.barh(x-width/2 , to , width, label='Turnovers')
rects2 = ax.barh(x+width/2 , played , width, label='Games Played')

ax.set_yticks(x,names)


plt.legend()


plt.show()