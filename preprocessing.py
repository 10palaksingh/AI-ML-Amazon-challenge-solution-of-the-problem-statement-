from pathlib import Path
import re
import pandas as pd
import unidecode

ROOT = Path(__file__).resolve().parents[1]
TRAIN_DIR = ROOT / "data" / "train"
TEST_DIR = ROOT / "data" / "test"
OUTPUT_DIR = ROOT / "output"
MODEL_DIR = ROOT / "models"

def normalize_text(value):
    if pd.isna(value):
        return ""
    text = str(value).lower()
    text = unidecode.unidecode(text)
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def prepare_source(df):
    df = df.copy()
    df["name_norm"] = df["business_name"].apply(normalize_text)
    df["address_norm"] = df["business_address"].apply(normalize_text)
    df["country_norm"] = df["country"].fillna("").astype(str).str.lower().str.strip()
    return df
