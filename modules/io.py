from rightmove_webscraper import rightmove_data
import pandas as pd


def get_and_save():
    print("downlaoding data...")
    url = "https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=STATION%5E1388&insId=1&radius=2.0&minPrice=170000&maxPrice=230000&minBedrooms=2&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"
    rightmove_object = rightmove_data(url)
    df = rightmove_object.get_results

    print(df.columns)

    # extract the data so that pandas doesn't complain about losing nanosecond info
    df.search_date = df.search_date.dt.date

    df.search_date = pd.to_datetime(df.search_date)
    df.to_parquet('data/bris_df.parquet', compression=None)


def load():
    print("loading data...")
    df = pd.read_parquet('data/bris_df.parquet')
    return df
