import os

# Directory paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CLIMATE_DATA_DIR = os.path.join(DATA_DIR, 'climate_data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')

# Climatology and DFI parameters
BASELINE_PERIOD = (1981, 2010)
ROLLING_WINDOW_DAYS = 30
PRECIP_THRESHOLD = 5.0  # mm/day
TEMP_MIN = 20.0  # °C
TEMP_MAX = 30.0  # °C
