import numpy as np 
import pandas as pd

#load the datasets
inspections = pd.read_csv("inspections.csv")
prices = pd.read_csv("prices.csv")
sales_samples = pd.read_csv("sales_samples.csv")

#set date column as datetime, then sort the values
for df in [inspections, prices, sales_samples]:
    df["date"] = pd.to_datetime(df["date"])
    df.sort_values("date", inplace=True)

'''
Join inspections with sales_samples by nearest date and stall (same week) 
to estimate expected loss per transaction
'''

inspections_sales_merge = pd.merge_asof(sales_samples, inspections, on="date",
    by="stall_id", direction="nearest", tolerance=pd.Timedelta("7 days"))

'''
Bring avg_price_per_kg from prices via key: date, market_id, commodity;
if dates don’t align,use last‐observation‐carried‐forward within 7 days
'''

all_merge = pd.merge_asof(inspections_sales_merge, prices, on="date", 
    by=["market_id", "commodity"], direction="backward",tolerance=pd.Timedelta("7 days"))





