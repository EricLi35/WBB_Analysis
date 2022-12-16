import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

dates = [
    datetime(2019,5,24),
    datetime(2019,5,25),
    datetime(2019,5,26),
    datetime(2019,5,27),
    datetime(2019,5,28),
    datetime(2019,5,29),
    datetime(2019,5,30)
]

y = [0,1,3,4,5,6,7]


plt.plot(dates,y)

plt.show()