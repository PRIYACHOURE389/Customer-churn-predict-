import pandas as pd
import os

BASE_DIR = r
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "churn_clean.csv")

df = pd.read_csv(DATA_PATH)
df.head()
"""
Data Preprocessing Module
-------------------------
Handles raw data loading and cleaning for the
Telco Customer Churn project.

Input:
- data/raw/telco_churn.csv

Output:
- data/processed/churn_clean.csv
"""

import pandas as pd
import numpy as np
import os


def load_raw_data(path: str) -> pd.DataFrame:
    """Load raw Telco churn dataset."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Core data cleaning steps:
    - Convert TotalCharges to numeric
    - Handle missing values
    - Standardize categorical columns
    """

    df = df.copy()

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Missing TotalCharges correspond to tenure = 0
    df["TotalCharges"].fillna(0.0, inplace=True)

    # Strip whitespace from categorical columns
    cat_cols = df.select_dtypes(include="object").columns
    df[cat_cols] = df[cat_cols].apply(lambda x: x.str.strip())

    return df


def save_clean_data(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned dataset to disk."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":

    BASE_DIR = os.path.dirname(__file__)
    RAW_DATA_PATH = os.path.join(BASE_DIR, "..", "data", "raw", "telco_churn.csv")
    OUTPUT_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "churn_clean.csv")

    df_raw = load_raw_data(RAW_DATA_PATH)
    df_clean = clean_data(df_raw)
    save_clean_data(df_clean, OUTPUT_PATH)

    print("Data preprocessing completed. Clean file saved to:")
    print(OUTPUT_PATH)

