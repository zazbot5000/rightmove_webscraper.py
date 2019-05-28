from rightmove_webscraper import rightmove_data
import pandas as pd


def scan_and_save(area_type):
    print("\nscraping RightMove web data...")

    radius = "2.0"
    minPrice = "160000"
    maxPrice = "264000"
    maxDaysSinceAdded = ""

    if area_type == "radius":
        # radius from temple meads
        url = f"https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=STATION%5E1388&insId=1&radius={radius}&minPrice={minPrice}&maxPrice={maxPrice}&minBedrooms=2&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"
    else:
        # polylines area
        # wide
        # locationIdentifier = """USERDEFINEDAREA%5E%7B"polylines"%3A"scdyHhd~NiF%7DgAaYgQwSgg%40kJec%40tGcb%40v%5Dss%40vU%7BZjTst%40_B_d%40jOql%40tPc%5EzPiRdSbApKzDzFp%5DjL_%5Dbk%40iRd%7B%40vg%40lXePvQvaB~N%7CgA%7CeAljCya%40paAco%40bAc_%40xv%40yi%40naAwe%40bAgsAd_%40od%40od%40ae%40%7Bh%40"%7D"""
        # tight
        locationIdentifier = """USERDEFINEDAREA%5E%7B"polylines"%3A"%7DjdyHj%7B%7BNaYgQwSgg%40kJec%40tGcb%40v%5Dss%40vU%7BZjTst%40_B_d%40jOql%40tPc%5EzPiRdSbApKzDfOhh%40tJkL%60SoM~KzKrT%7CLzX%7CTd%60%40pr%40%7CEpw%40kHndAiGvYrEx%7D%40xR%7Cq%40wNb%7B%40yi%40naAwe%40bAgsAd_%40od%40od%40ae%40%7Bh%40iF%7DgA"%7D"""

        url = f"""https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier={locationIdentifier}&minPrice={minPrice}&maxPrice={maxPrice}&minBedrooms=2&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded={maxDaysSinceAdded}&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"""

    rightmove_object = rightmove_data(url)
    df = rightmove_object.get_results
    df.to_parquet("data/houses_for_sale.parquet.gzip", compression="gzip")
    print("\tweb data scraped!")


def load():
    print("loading data...")
    df = pd.read_parquet("data/houses_for_sale.parquet.gzip")
    return df
