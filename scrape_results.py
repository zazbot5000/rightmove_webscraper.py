from modules import io, analysis, gdrive_tools


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

    if args.scrape or args.complete:
        io.get_and_save()

    if args.analyse or args.complete:
        df = io.load()
        analysis.analyse(df)

    if args.upload or args.complete:
        gdrive_tools.upload_csv()


if __name__ == "__main__":
    args_main = get_parser().parse_args()

    main(args_main)
