import numpy as np
import pandas as pd

np.random.seed(2)

'For generating prices.csv'

#random amount of days chosen between 60-120
days = np.random.randint(60, 121)

# Inspection dates, starts at 2026-01-01, weekly every Thursday, same as inspections.csv 
date = pd.date_range(start='2026-01-01', periods=days, freq='W-THU')

market_id = np.random.randint(1, 6, size=days) #Market ID - 1-5 Markets

commodity = None
avg_price_per_kg = None