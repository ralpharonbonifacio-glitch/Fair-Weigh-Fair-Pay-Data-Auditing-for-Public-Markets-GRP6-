import numpy as np
import pandas as pd

np.random.seed(2)

'For generating prices.csv'

#random amount of days chosen between 60-120
days = np.random.randint(60, 121)

# Inspection dates, starts at 2026-01-01, weekly every Thursday, same as inspections.csv 
date = pd.date_range(start='2026-01-01', periods=days, freq='W-THU')

market_id = np.random.randint(1, 6, size=days) #Market ID - 1-5 Markets

#commodities logic
#commodity list, 8-12 choices
commodity_list = [ 'Rice', 'Chicken', 'Pork', 'Beef', 
                  'Bangus', 'Tomatoes', 'Onions', 'Garlic', 
                  'Eggplant', 'Cabbage', 'Carrots', 'Potatoes', 
                  'Tilapia', 'Ginger']

commodity_amount = np.random.randint(8, 13) #commodity_amount, choose random amount of commodities in the list

#code for choosing which commodities are chosen, replace=False for no duplicates and keep all distinct
commodities_chosen = np.random.choice(commodity_list, size=commodity_amount, replace=False)

#Assign the chosen commodities to your rows
commodity = np.random.choice(commodities_chosen, size=days)


avg_price_per_kg = None