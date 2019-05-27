from modules import scraper, analyser, gdrive_io


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
        description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-s",
        "--scrape",
        action="store_true",
        help="scrape data from the rightmove website",
    )
    parser.add_argument(
        "-a",
        "--analyse",
        action="store_true",
        help="load data from local files and analyse",
    )
    parser.add_argument(
        "-u", "--upload", action="store_true", help="upload data to google drive"
    )
    parser.add_argument(
        "-c", "--complete", action="store_true", help="run the complete workflow"
    )

    return parser


def main(args):

    for area_type in ["radius", "poly"]:
        if args.scrape or args.complete:
            scraper.get_and_save(area_type)

        if args.analyse or args.complete:
            df = scraper.load()
            analyser.analyse(df)

        if args.upload or args.complete:
            gdrive_io.upload_csv(area_type)


if __name__ == "__main__":
    args_main = get_parser().parse_args()

    main(args_main)
