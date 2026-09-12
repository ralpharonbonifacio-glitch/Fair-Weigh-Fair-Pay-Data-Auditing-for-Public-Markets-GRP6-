'For generating inspections.csv'

# Inspection dates, starts at 2026-01-01, 16 weeks, every Thursday
date = None

market_id = None #Market ID -> 1-5 Markets
stall_id = None #Stall ID -> 30-50 Stalls
scale_id = None #Scale ID -> 1-2 Scales per Stall
inspector_id = None #Inspector ID - 1-5 Inspectors

#certifcation date logic
is_certified = None #Check if inspector is certified
last_cert_date = None #latest cert date for inspector
is_certified = None #Check if inspector last cert date is within 365 days, else expired

#Weight calculation
nominal_weight_g = None #test weights
reading_g = None #Actual weight reading after test
