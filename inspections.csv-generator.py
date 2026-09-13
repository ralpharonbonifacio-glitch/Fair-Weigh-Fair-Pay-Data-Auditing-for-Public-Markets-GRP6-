import numpy as np
import pandas as pd

np.random.seed(1)

'For generating inspections.csv'

#random amount of days chosen between 60-120
days = np.random.randint(60, 121)

# Inspection dates, starts at 2026-01-01, weekly every Thursday
date = pd.date_range(start='2026-01-01', periods=days, freq='W-THU')

#IDs
market_id = np.random.randint(1, 6, size=days) #Market ID - 1-5 Markets
stall_id = np.random.randint(30, 51,size=days) #Stall ID - 30-50 Stalls
scale_id = np.random.randint(1, 3, size=days) #Scale ID - 1 or 2 Scales per Stall
inspector_id = np.random.randint(1, 6, size=days) #Inspector ID - 1-5 Inspectors

#certifcation date logic
randdays = np.random.randint(30, 501, size=days) #random amount of days for synthetic data generation
last_cert_date = (date - pd.to_timedelta(randdays, unit="D")).strftime("%Y-%m-%d")
is_certified = np.where(randdays <= 365, "Y", "N") #Check if inspector last cert date is within 365 days, else expired


#Convert date as data to make sure it can run
date_as_data = date.strftime("%Y-%m-%d")


#weight calibration
#Nominal Weight tests - 100g, 250g, 500g, 1000g
nominal_weight_g = np.random.choice([100, 250, 500, 1000], size=days)

#Error percentage, Minimum and maximum of at least and at most 75% to simulate possible fraud
error_perc = np.random.uniform(-0.02, 0.02, size=days)

#Reading Weight from using scale, difference varies based on error percentage
reading_g = np.round(nominal_weight_g * (1 + error_perc), 2)

#Create dataframe
df_inspections = pd.DataFrame({
    "date": date_as_data,
    "market_id": market_id,
    "stall_id": stall_id,
    "scale_id": scale_id,
    "nominal_weight_g": nominal_weight_g,
    "reading_g": reading_g,
    "is_certified": is_certified,
    "last_cert_date": last_cert_date,
    "inspector_id": inspector_id
})

# 7. Save to CSV
df_inspections.to_csv("inspections.csv", index=False)
print("inspections.csv created")
print(df_inspections.head())
