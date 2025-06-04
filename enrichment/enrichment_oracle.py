import pandas as pd
from .climate_loader import load_precip_data, load_temp_data
from .climatology import calculate_climatology
from .dfi_calc import generate_dfi_anomaly
from utils import config

def run_oracle():
    # Load data
    practice_logs = pd.read_csv(f"{config.DATA_DIR}/practice_logs.csv")
    precip_ds = load_precip_data()
    temp_ds = load_temp_data()

    # Generate climatology
    climatology = calculate_climatology(precip_ds, config.BASELINE_PERIOD)

    # Parameters for enrichment
    params = {
        'window_days': config.ROLLING_WINDOW_DAYS,
        'precip_threshold': config.PRECIP_THRESHOLD,
        'temp_min': config.TEMP_MIN,
        'temp_max': config.TEMP_MAX
    }

    enriched_rows = []

    for idx, row in practice_logs.iterrows():
        dfi, clim_mean, anomaly = generate_dfi_anomaly(row, precip_ds, temp_ds, climatology, params)
        enriched_rows.append({
            'plot_id': row['plot_id'],
            'date': row['date'],
            'practice': row['practice'],
            'dfi': dfi,
            'dfi_climatology': clim_mean,
            'dfi_anomaly': anomaly
        })

    enriched_df = pd.DataFrame(enriched_rows)
    enriched_df.to_csv(f"{config.OUTPUT_DIR}/enriched_logs.csv", index=False)
    print("Enrichment completed. Output written to /output/enriched_logs.csv")
