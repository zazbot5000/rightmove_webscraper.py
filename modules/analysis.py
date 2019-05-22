import pandas as pd
import numpy as np


def sanitize(df):
    print("\tsanitising...")

    df = df.drop_duplicates()
    df = df.sort_values("time_in_market", ascending=False)
    df = df.loc[df["time_in_market"].str.contains('/05/2019', regex=False)]

    df["number_bedrooms"] = pd.to_numeric(df["number_bedrooms"], errors='coerce').astype(np.int64)

    return df


def grouped_print(df):

    grouped_df = df.groupby("number_bedrooms")
    # print the grouped results

    # for i in reversed(range(1, 6)):
    #     try:
    #         print(
    #             grouped_df.get_group(i)[
    #                 ["number_bedrooms", "price", "time_in_market", "url"]
    #             ],
    #             "\n",
    #         )
    #     except:
    #         pass

    print(grouped_df.aggregate(np.mean))

def rank(df):
    print("ranking...")
    print(df.columns)

    # ['price', 'type', 'address', 'url', 'agent_url', 'time_in_market',
    #  'postcode', 'number_bedrooms', 'search_date']
    # print(df["type"].unique())

    pd.options.display.max_colwidth = 200

    df = sanitize(df)

    new_df = df.sort_values(["number_bedrooms", "time_in_market"], ascending=False)
    print(new_df[["number_bedrooms", "price", "time_in_market", "url"]])
    new_df.to_csv(r'output\export_dataframe.csv', index=None, header=True)
