import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')
names = []
blocks = []

for i in range(len(data['BLOCKS'])):
    if data['BLOCKS'][i] != 0:
        print(data['PLAYER'][i] + " got at least 1 block")
        names.append(data['PLAYER'][i])
        blocks.append(data['BLOCKS'][i])


fig,ax = plt.subplots()
ax.pie(blocks, labels=names , autopct='%1.1f%%')

ax.set_title("Allocation of Blocks, out of "+str(data['BLOCKS'].sum())+" Combined Blocks (Game Totals)")

plt.show()
