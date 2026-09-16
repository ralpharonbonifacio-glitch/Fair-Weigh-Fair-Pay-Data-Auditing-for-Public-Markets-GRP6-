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

all_merge["loss_php"] = (
    np.maximum(
        0,
        all_merge["label_weight_kg"]
        - all_merge["actual_weight_kg"]
    )
    * all_merge["avg_price_per_kg"]
)

all_merge["is_under_weigh"] = (
    all_merge["actual_weight_kg"]
    < all_merge["label_weight_kg"]
)

all_merge["error_weight_perc"] = (
    (
        all_merge["actual_weight_kg"]
        - all_merge["label_weight_kg"]
    )
    / all_merge["label_weight_kg"]
) * 100

rollingrate = (
    all_merge
    .set_index("date")
    .sort_index()
)

market_rolling_rate = (
    rollingrate
    .groupby("market_id")["is_under_weigh"]
    .rolling("14D")
    .mean()
)

markets = sorted(all_merge["market_id"].unique())

plt.figure(figsize=(10, 6))

for market in markets:

    market_data = market_rolling_rate[market]

    plt.plot(
        market_data.index,
        market_data.values * 100,
        label="Market " + str(market)
    )

plt.xlabel("Date")
plt.ylabel("14-Day Rolling Under-Weigh Rate (%)")
plt.title("14-Day Rolling Under-Weigh Rate by Market")

plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

