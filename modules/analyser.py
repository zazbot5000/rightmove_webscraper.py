from pathlib import Path
import pandas as pd
import numpy as np


def sanitize(df):
    print("\tsanitising...")

    df = df.drop_duplicates()
    df = df.sort_values("activity date", ascending=False)
    df = df.loc[df["activity date"].str.contains("/05/2019", regex=False)]

    df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce").astype(np.int64)

    return df


def grouped_print(df):

    grouped_df = df.groupby("bedrooms")
    print(grouped_df.aggregate(np.mean))


def analyse(df):
    print("analysing data...")
    pd.options.display.max_colwidth = 200
    df = sanitize(df)

    print("\tsorting...")
    new_df = df.sort_values(["bedrooms", "activity date"], ascending=False)

    print("\texporting to csv...")
    new_df.to_csv(Path("data/export_dataframe.csv"), index=None, header=True)

    print("\tanalysis complete!")
