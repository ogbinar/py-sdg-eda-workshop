COUNTRIES = {
    "Philippines": "PHL",

    # ASEAN peers
    "Vietnam": "VNM",
    "Indonesia": "IDN",
    "Thailand": "THA",
    "Malaysia": "MYS",

    # Large emerging
    "India": "IND",
    "China": "CHN",

    # Advanced economy
    "Singapore": "SGP",
    "Japan": "JPN",        # swapped US — more regionally relevant benchmark
    "United States": "USA", # keep for global anchor
}

COUNTRY_GROUP = {
    "Philippines": "Philippines",

    "Vietnam": "ASEAN peer",
    "Indonesia": "ASEAN peer",
    "Thailand": "ASEAN peer",
    "Malaysia": "ASEAN peer",

    "India": "Large emerging",
    "China": "Large emerging",

    "Singapore": "Advanced economy",
    "Japan": "Advanced economy",
    "United States": "Advanced economy",
}

INDICATORS = {
    # --- Human Capital ---
    "education_secondary": "WB_WDI_SE_SEC_CUAT_UP_ZS",   # Educational attainment, at least upper secondary (%)
    "education_expenditure": "WB_WDI_SE_XPD_TOTL_GD_ZS", # Gov't expenditure on education (% of GDP)  [governance proxy]

    # --- Digital Infrastructure ---
    "internet_users_pct": "WB_WDI_IT_NET_USER_ZS",       # Internet users (% of population)

    # --- Economic Development ---
    "gdp_per_capita": "WB_WDI_NY_GDP_PCAP_CD",           # GDP per capita (current US$)

    # --- Poverty / Inclusion ---
    "poverty_headcount": "WB_WDI_SI_POV_NAHC",           # Poverty headcount ratio (% of population)
    "gini_index": "WB_WDI_SI_POV_GINI",                  # Gini index (inequality) — sparse, use LOV

    # --- Human Wellbeing ---
    "life_expectancy": "WB_WDI_SP_DYN_LE00_IN",          # Life expectancy at birth (years)
    "hospital_beds": "WB_WDI_SH_MED_BEDS_ZS",            # Hospital beds per 1,000 people

    # --- Environment ---
    "co2_per_capita": "WB_WDI_EN_ATM_CO2E_PC",           # CO2 emissions per capita (tonnes)

    # --- Mobility ---
    "air_passengers": "WB_WDI_IS_AIR_PSGR",              # Air transport, passengers carried

    # --- Context (not for comparison charts) ---
    "population_total": "WB_WDI_SP_POP_TOTL",            # Total population
}

# Indicators used for the deep-dive analysis (trends, scatter, ranking, composite index)
CORE_INDICATORS = [
    "education_secondary",
    "internet_users_pct",
    "gdp_per_capita",
    "poverty_headcount",
    "life_expectancy",
]

# Indicators shown only in the context snapshot chart — fulfill promo coverage without extra deep-dive time
CONTEXT_INDICATORS = [
    "gini_index",
    "hospital_beds",
    "co2_per_capita",
    "air_passengers",
    "education_expenditure",
]

DATABASE_ID = "WB_WDI"
BASE_URL = "https://data360api.worldbank.org"

TIME_FROM = 2000
TIME_TO = 2025

RAW_DIR = "data/raw"
CURATED_DIR = "data/curated"
LOG_DIR = "data/logs"
