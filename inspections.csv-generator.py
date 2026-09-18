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

#certifcation date logic

inspector_id = np.random.randint(1, 6, size=days) #Inspector ID - 1-5 Inspectors

inspector_certificate = pd.to_datetime('2026-01-01') - pd.to_timedelta(np.random.randint(12, 30, size=6), unit="D") #Create set dates for inspector certificates

last_cert_check = pd.DatetimeIndex(inspector_certificate[inspector_id]) #assign inspector certificate values to inspector id

check_cert = (date - last_cert_check).days #calculate if its still valid

is_certified = np.where(check_cert <= 548, "Y", "N") #Check if inspector last cert date is within  548 days (1.5 years), else expired

last_cert_date = last_cert_check.strftime("%Y-%m-%d") #turn last cert check to string with format year-month-day

#Convert date as data to make sure it can run
date_as_data = date.strftime("%Y-%m-%d")


#weight calibration
#Nominal Weight tests - 100g, 250g, 500g, 1000g
nominal_weight_g = np.random.choice([100, 250, 500, 1000], size=days)

#Error percentage
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
