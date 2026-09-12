import numpy as np
import pandas as pd

np.random.seed(1)

'For generating inspections.csv'

# Inspection dates, starts at 2026-01-01, 16 weeks, every Thursday
date = pd.date_range(start='2026-01-01', periods=16, freq='W-THU')

#IDs
market_id = np.random.randint(1, 6, size=16) #Market ID - 1-5 Markets
stall_id = np.random.randint(30, 51,size=16) #Stall ID - 30-50 Stalls
scale_id = np.random.randint(1, 2, size=16) #Scale ID - 1 or 2 Scales per Stall
inspector_id = np.random.randint(1, 6, size=16) #Inspector ID - 1-5 Inspectors

#certifcation date logic
is_certified = None #Check if inspector is certified
last_certs_date = None #latest cert date for inspector
is_certified = None #Check if inspector last cert date is within 365 days, else expired

#Weight calculation
nominal_weight_g = None #test weights
reading_g = None #Actual weight reading after test
