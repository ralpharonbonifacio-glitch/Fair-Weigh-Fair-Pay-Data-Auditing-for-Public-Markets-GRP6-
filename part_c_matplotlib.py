import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

inspections = pd.read_csv("inspections.csv")
prices = pd.read_csv("prices.csv")
sales_samples = pd.read_csv("sales_samples.csv")

print("Inspections:", inspections.shape)
print("Prices:", prices.shape)
print("Sales samples:", sales_samples.shape)

inspections["date"] = pd.to_datetime(inspections["date"])
prices["date"] = pd.to_datetime(prices["date"])
sales_samples["date"] = pd.to_datetime(sales_samples["date"])

inspections.sort_values("date", inplace=True)
prices.sort_values("date", inplace=True)
sales_samples.sort_values("date", inplace=True)

inspections_sales_merge = pd.merge_asof(
    sales_samples,
    inspections,
    on="date",
    by=["stall_id", "market_id"],
    direction="nearest",
    tolerance=pd.Timedelta("7 days")
)

all_merge = pd.merge_asof(
    inspections_sales_merge,
    prices,
    on="date",
    by=["market_id", "commodity"],
    direction="backward",
    tolerance=pd.Timedelta("7 days")
)
