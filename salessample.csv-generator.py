import numpy as np
import pandas as pd

np.random.seed(3)

'For generating sales_samples.csv'

df_inspections = pd.read_csv("inspections.csv")
df_prices = pd.read_csv("prices.csv")
date = np.random.choice(df_inspections['date'].unique(), size=len(df_inspections))
market_id = np.random.choice(df_inspections['market_id'].values, size=len(df_inspections))
stall_id = np.random.choice(df_inspections['stall_id'].values, size=len(df_inspections))

commodity_list = ['Rice', 'Chicken', 'Pork', 'Beef',
                  'Bangus', 'Tomatoes', 'Onions', 'Garlic',
                  'Eggplant', 'Cabbage', 'Carrots', 'Potatoes',
                  'Tilapia', 'Ginger']

commodities_chosen = df_prices['commodity'].unique()
commodity = np.random.choice(commodities_chosen, size=len(df_inspections))

label_weight_kg = np.random.choice(
    [0.5, 1.0, 1.5, 2.0],
    size=len(df_inspections))

error_perc = np.random.uniform(-0.0075, 0.0025, size=len(df_inspections))
actual_weight_kg = np.round(label_weight_kg * (1 + error_perc), 3)
price_lookup = df_prices[['date', 'market_id', 'commodity', 'avg_price_per_kg']]

df_sales = pd.DataFrame({
    'date': date,
    'market_id': market_id,
    'stall_id': stall_id,
    'commodity': commodity,
    'label_weight_kg': label_weight_kg,
    'actual_weight_kg': actual_weight_kg})

df_sales = df_sales.merge(
    price_lookup,
    on=['date', 'market_id', 'commodity'],
    how='left')

paid_amount_php = np.round(
    df_sales['label_weight_kg'] *
    df_sales['avg_price_per_kg'],
    2)

df_sales['paid_amount_php'] = paid_amount_php
df_sales = df_sales[
       ['date',
        'market_id',
        'stall_id',
        'commodity',
        'paid_amount_php',
        'label_weight_kg',
        'actual_weight_kg']]
df_sales.to_csv("sales_samples.csv", index=False)
print("sales_samples.csv created")
print(df_sales.head())
