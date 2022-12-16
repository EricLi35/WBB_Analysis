import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("PLAYER_DATA\Player_Data.csv" , sep='\t')

list = []
for height in data['Height_cm']:
    if height not in list:
        list.append(height)

list.sort()
# the bins are:
# [167.64, 172.72, 177.8, 180.34, 182.88, 185.42, 187.96, 198.12]
# print(list)


# list2 = []
# for height in data['Height_ft']:
#     if height not in list2:
#         list2.append(height)
# list2.sort()
# print(list2)

plt.hist(data['Height_cm'], bins=list , edgecolor='black')
plt.title("Height of Players and their Frequencies")
plt.xlabel("Height of Player (cm)")
plt.ylabel("Number of Players Between Specified Height Range")
plt.xticks(list)
plt.show()



# input = 'python'
# outputEven = ''

# for index, element in enumerate(list(input)):
# 	if index % 2 == 0:
# 		outputEven += element

# print(outputEven)
