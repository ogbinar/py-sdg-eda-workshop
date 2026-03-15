import pandas as pd


def clean_indicator_df(
    df: pd.DataFrame,
    country_name: str,
    country_code: str,
    country_group: str,
    indicator_name: str,
    indicator_code: str,
) -> pd.DataFrame:
    """
    Standardize schema and append metadata columns.
    """
    if df.empty:
        return df

    df = df.copy()

    if "OBS_VALUE" in df.columns:
        df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")

    if "TIME_PERIOD" in df.columns:
        df["TIME_PERIOD"] = pd.to_numeric(
            df["TIME_PERIOD"], errors="coerce"
        ).astype("Int64")

    df["country"] = country_name
    df["country_code"] = country_code
    df["country_group"] = country_group
    df["indicator"] = indicator_name
    df["indicator_code"] = indicator_code

    preferred_cols = [
        "country",
        "country_code",
        "country_group",
        "indicator",
        "indicator_code",
        "TIME_PERIOD",
        "OBS_VALUE",
    ]

    other_cols = [c for c in df.columns if c not in preferred_cols]
    df = df[preferred_cols + other_cols]

    df = df.sort_values(
        ["country_group", "country", "indicator", "TIME_PERIOD"]
    ).reset_index(drop=True)

    return df