import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

inspections = pd.read_csv("inspections.csv")
prices = pd.read_csv("prices.csv")
sales_samples = pd.read_csv("sales_samples.csv")

print("Inspections:", inspections.shape)
print("Prices:", prices.shape)
print("Sales samples:", sales_samples.shape)
