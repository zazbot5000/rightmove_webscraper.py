from rightmove_webscraper import rightmove_data
import pandas as pd


def get_and_save(area_type):
    print("\nscraping RightMove web data...")

    radius = "2.0"
    minPrice = "170000"
    maxPrice = "264000"

    if area_type == "radius":
        # radius from temple meads
        url = f"https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=STATION%5E1388&insId=1&radius={radius}&minPrice={minPrice}&maxPrice={maxPrice}&minBedrooms=2&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"
    else:
        # polylines area
        url = f"""https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=USERDEFINEDAREA%5E%7B"polylines"%3A"scdyHhd~NiF%7DgAaYgQwSgg%40kJec%40tGcb%40v%5Dss%40vU%7BZjTst%40_B_d%40jOql%40tPc%5EzPiRdSbApKzDzFp%5DjL_%5Dbk%40iRd%7B%40vg%40lXePvQvaB~N%7CgA%7CeAljCya%40paAco%40bAc_%40xv%40yi%40naAwe%40bAgsAd_%40od%40od%40ae%40%7Bh%40"%7D&minPrice={minPrice}&maxPrice={maxPrice}&minBedrooms=2&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"""
    rightmove_object = rightmove_data(url)
    df = rightmove_object.get_results

    # extract the data so that pandas doesn't complain about losing nanosecond info
    df.search_date = df.search_date.dt.date

    df.search_date = pd.to_datetime(df.search_date)
    df.to_parquet("data/houses_for_sale.parquet.gzip", compression="gzip")
    print("\tweb data scraped!")


def load():
    print("loading data...")
    df = pd.read_parquet("data/houses_for_sale.parquet.gzip")
    return df
