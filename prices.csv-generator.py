import numpy as np
import pandas as pd

np.random.seed(2)

'For generating prices.csv'

#random amount of days chosen between 60-120
days = np.random.randint(60, 121)

# Inspection dates, starts at 2026-01-01, weekly every Thursday, same as inspections.csv, 
# strftime to make sure its a string in format Year-month-day
date = pd.date_range(start='2026-01-01', periods=days, freq='W-THU').strftime("%Y-%m-%d")



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

#created minmax bound for avg_price_per_kg so each item price is different and actually makes sense for a synthetic

commodity_price_minmax = {
    'Rice': (45.0, 60.0),
    'Chicken': (180.0, 220.0),
    'Pork': (300.0, 380.0),
    'Beef': (350.0, 450.0),
    'Bangus': (160.0, 220.0),
    'Tomatoes': (60.0, 120.0),
    'Onions': (80.0, 150.0),
    'Garlic': (100.0, 180.0),
    'Eggplant': (60.0, 90.0),
    'Cabbage': (80.0, 140.0),
    'Carrots': (90.0, 150.0),
    'Potatoes': (90.0, 140.0),
    'Tilapia': (120.0, 160.0),
    'Ginger': (100.0, 160.0)
}

#pull bounds, commodity_price_minmax(dictionary)[x][0] to call min value, [x][1] to call for max, 
#for x in commodity so it calls for each name in list
minprice = [commodity_price_minmax[x][0] for x in commodity]
maxprice = [commodity_price_minmax[x][1] for x in commodity]

#calculate average price per kg from each unique commodity
avg_price_per_kg = np.round(np.random.uniform(minprice, maxprice), 2)

df_prices = pd.DataFrame({
    'date': date,
    'market_id': market_id,
    'commodity': commodity,
    'avg_price_per_kg': avg_price_per_kg
})

df_prices.to_csv("prices.csv", index=False)
print("Generated prices.csv")
print(df_prices.head())