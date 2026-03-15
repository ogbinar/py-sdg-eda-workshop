import os
import json
import logging
from datetime import datetime

import pandas as pd

from src.config import (
    COUNTRIES,
    COUNTRY_GROUP,
    INDICATORS,
    DATABASE_ID,
    BASE_URL,
    TIME_FROM,
    TIME_TO,
    RAW_DIR,
    CURATED_DIR,
    LOG_DIR,
)
from src.extract import fetch_indicator_data
from src.transform import clean_indicator_df


def setup_directories():
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(CURATED_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)


def setup_logger():
    log_file = os.path.join(LOG_DIR, "pipeline.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ],
    )


def run_pipeline():
    setup_directories()
    setup_logger()

    all_cleaned = []
    manifest = []
    run_ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    logging.info("Pipeline started")

    for country_name, country_code in COUNTRIES.items():
        for indicator_name, indicator_code in INDICATORS.items():
            logging.info(f"Fetching {country_name} | {indicator_name}")

            record = {
                "run_ts": run_ts,
                "country": country_name,
                "country_code": country_code,
                "country_group": COUNTRY_GROUP.get(country_name, "Unknown"),
                "indicator": indicator_name,
                "indicator_code": indicator_code,
                "status": "success",
                "rows": 0,
                "error": None,
            }

            try:
                raw_df = fetch_indicator_data(
                    base_url=BASE_URL,
                    database_id=DATABASE_ID,
                    indicator=indicator_code,
                    ref_area=country_code,
                    time_from=TIME_FROM,
                    time_to=TIME_TO,
                )

                raw_filename = (
                    f"{country_name.lower().replace(' ', '_')}__"
                    f"{indicator_name}.csv"
                )
                raw_path = os.path.join(RAW_DIR, raw_filename)
                raw_df.to_csv(raw_path, index=False)

                clean_df = clean_indicator_df(
                    raw_df,
                    country_name=country_name,
                    country_code=country_code,
                    country_group=COUNTRY_GROUP.get(country_name, "Unknown"),
                    indicator_name=indicator_name,
                    indicator_code=indicator_code,
                )

                record["rows"] = len(clean_df)

                if not clean_df.empty:
                    all_cleaned.append(clean_df)

            except Exception as e:
                logging.exception(f"Failed: {country_name} | {indicator_name}")
                record["status"] = "failed"
                record["error"] = str(e)

            manifest.append(record)

    manifest_df = pd.DataFrame(manifest)
    manifest_path = os.path.join(CURATED_DIR, f"manifest_{run_ts}.csv")
    manifest_df.to_csv(manifest_path, index=False)

    if all_cleaned:
        final_df = pd.concat(all_cleaned, ignore_index=True)

        csv_path = os.path.join(CURATED_DIR, f"worldbank_indicators_{run_ts}.csv")
        parquet_path = os.path.join(CURATED_DIR, f"worldbank_indicators_{run_ts}.parquet")

        final_df.to_csv(csv_path, index=False)
        final_df.to_parquet(parquet_path, index=False)

        logging.info(f"Saved curated CSV: {csv_path}")
        logging.info(f"Saved curated Parquet: {parquet_path}")
    else:
        logging.warning("No data collected. Curated dataset not written.")

    logging.info(f"Saved manifest: {manifest_path}")
    logging.info("Pipeline finished")


if __name__ == "__main__":
    run_pipeline()
