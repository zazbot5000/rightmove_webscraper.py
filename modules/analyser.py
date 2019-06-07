from pathlib import Path
import pandas as pd
import numpy as np


def sanitize(df):
    print("\tsanitising...")

    df.drop_duplicates(inplace=True)
    df.loc[:, "bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce").astype(np.int64)
    df.loc[:, "activity datetime"] = pd.to_datetime(df["activity date"], format='%d/%m/%Y')

    return df


def grouped_print(df):

    grouped_df = df.groupby("bedrooms")
    print(grouped_df.aggregate(np.mean))


def analyse(df):
    print("analysing data...")
    pd.options.display.max_colwidth = 200
    df = sanitize(df)

    print("\tsorting...")
    df = df.sort_values(["bedrooms", "activity datetime"], ascending=False)
    df = df.drop(columns="activity datetime")

    print("\texporting to csv...")
    df.to_csv(Path("data/export_dataframe.csv"), index=None, header=True)

    print("\tanalysis complete!")
