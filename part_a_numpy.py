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
