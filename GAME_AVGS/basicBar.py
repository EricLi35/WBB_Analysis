import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("GAME_AVGS\GameAvgAnalysis.csv")

names = data['PLAYER']
twoptt = data['2 PTT']
twoptm = data['2 PTM']


print(type(twoptt))


# print(data.head(3))


plt.bar(names,twoptm , width=0.5)

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light'
    )

plt.ylabel("2 Pointers Made")

plt.show()