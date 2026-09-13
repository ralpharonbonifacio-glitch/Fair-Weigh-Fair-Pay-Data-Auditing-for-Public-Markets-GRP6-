import numpy as np
import pandas as pd

df = pd.read_csv("inspections.csv")

print(df.head())
print(df.shape)

# Calculate scale error
error_g = df["reading_g"].to_numpy() - df["nominal_weight_g"].to_numpy()
error_pct = (error_g / df["nominal_weight_g"].to_numpy()) * 100

print("Error in grams:")
print(error_g[:5])

print("Error in percent:")
print(error_pct[:5])

# Create masks for weighing errors
under_mask = error_pct < -0.5
over_mask = error_pct > 0.5
outside_mask = under_mask | over_mask

print("Under-weighing:")
print(under_mask[:10])

print("Over-weighing:")
print(over_mask[:10])

print("Outside tolerance:")
print(outside_mask[:10])

# Calculate mean and median error per market
market_ids = df["market_id"].to_numpy()
markets = np.unique(market_ids)

market_mask = market_ids[:, np.newaxis] == markets[np.newaxis, :]
market_errors = np.where(market_mask, error_pct[:, np.newaxis], np.nan)

mean_error = np.nanmean(market_errors, axis=0)
median_error = np.nanmedian(market_errors, axis=0)

print("Markets:", markets)
print("Mean error per market:", mean_error)
print("Median error per market:", median_error)

# Calculate 95% confidence interval
n = np.sum(~np.isnan(market_errors), axis=0)
std_error = np.nanstd(market_errors, axis=0, ddof=1) / np.sqrt(n)

margin_error = 1.96 * std_error

ci_lower = mean_error - margin_error
ci_upper = mean_error + margin_error

print("95% CI lower:", ci_lower)
print("95% CI upper:", ci_upper)
