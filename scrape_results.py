from modules import io, analysis, drive_upload


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

    return parser


def main(args):

    if args.scrape:
        io.get_and_save()
    elif args.analyse:
        df = io.load()
        analysis.rank(df)
    elif args.upload:
        service = drive_upload.g_authenticate()
        drive_upload.save_to_g_drive(service)


if __name__ == "__main__":
    args_main = get_parser().parse_args()

    main(args_main)
