# OBSOLETE, REFER TO doubleBarBOTH.py


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# data = pd.read_csv("GAME_TOTALS\GAME_TOTALS.csv" , sep='\t')
# names = data['PLAYER']
# threeptt = data['3 PTT']
# threeptm = data['3 PTM']

# x = np.arange(len(names))
# y = np.arange(0,70,10)

# width = 0.35
# fig, ax = plt.subplots()
# rects1 = ax.bar(x-width/2 , threeptt , width, label='3 pters attempted')
# rects2 = ax.bar(x+width/2 , threeptm , width, label='3 pters made' , color='#99cc00')

# ax.set_ylabel('Number of Shots')
# ax.set_title("Each player's 3 pt Makes and Attempted (Total Across All Games)")

# # Axes.set_xticks(ticks, labels=None) where ticks is list of tick locations (floats)
# # and labels (optional) is a list of strings that labels the ticks 
# ax.set_xticks(x, names)
# ax.set_yticks(y)

# # change the font size of the labels (in this case, x-axis and only the major ticks)
# ax.tick_params(axis='x', which='major', labelsize=9.5)

# ax.legend()

# # remove whitespace (found that it didn't seem to help, only worsened matters)
# # fig.tight_layout()

# # adjust rotation and boldness of (in this case, x-axis)
# plt.xticks(
#     rotation=45, 
#     horizontalalignment='right',
#     fontweight='light'
#     )

# ax.bar_label(rects1,padding=2,size=8.5)
# ax.bar_label(rects2,padding=2,size=8.5)

# # phyiscally change the dimensions of the plot when outputted 
# # (takes in values as the actual position (imagine a coordinate grid))
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.13)
# plt.show()