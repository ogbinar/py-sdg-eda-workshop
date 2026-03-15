import time
import requests
import pandas as pd


def fetch_indicator_data(
    base_url: str,
    database_id: str,
    indicator: str,
    ref_area: str,
    time_from: int,
    time_to: int,
    skip: int = 0,
    max_retries: int = 3,
    retry_delay: int = 2,
) -> pd.DataFrame:
    """
    Fetch one indicator for one country from Data360 API.
    Returns a pandas DataFrame.
    """
    url = f"{base_url}/data360/data"
    params = {
        "DATABASE_ID": database_id,
        "INDICATOR": indicator,
        "REF_AREA": ref_area,
        "timePeriodFrom": str(time_from),
        "timePeriodTo": str(time_to),
        "skip": skip,
    }

    last_error = None

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, params=params, timeout=60)
            response.raise_for_status()
            payload = response.json()

            df = pd.DataFrame(payload.get("value", []))
            return df

        except Exception as e:
            last_error = e
            if attempt < max_retries:
                time.sleep(retry_delay)
            else:
                raise last_error
