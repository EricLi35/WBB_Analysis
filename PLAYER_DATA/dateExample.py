import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("PLAYER_DATA\player5.csv" , sep='\t')
dates = []
twofg = []
threefg = []
fg = []

for i in range(len(data['Date'])):
    if data['FGT'][i] != 0 or data['2 PT%'][i] != '-':
        ex = data['Date'][i]
        ex = ex[0:len(ex)-4]
        dates.append((ex+ex[0:2])[3:])
        twofg.append(float(data['2 PT%'][i][0:len(data['2 PT%'][i])-1]))
        threefg.append(float(data['3 PT%'][i][0:len(data['3 PT%'][i])-1]))
        fg.append(float(data['FG %'][i][0:len(data['FG %'][i])-1]))


x = np.arange(len(dates))
y = np.arange(0,105,5)

fig,ax = plt.subplots()

line1 = ax.plot(x, twofg , label='2 pter fg%')
line2 = ax.plot(x, threefg , label='3 pter fg%')
line3 = ax.plot(x, fg , label='Overall fg%')

ax.set_xticks(x,dates)
ax.set_yticks(y)

ax.set_xlabel("Date")
ax.set_ylabel("Shooting Percentage")
ax.set_title("Hailey Counsell's 2pt, 3pt, and overall field goal percentages (Practices) ")

ax.legend()

plt.xticks(rotation = 45)

plt.show()