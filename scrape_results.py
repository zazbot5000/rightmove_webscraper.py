from modules import io, analysis


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
        description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-d",
        "--download_new",
        action="store_true",
        help="load data from local files if they exist",
    )

    return parser


def main(args):

    if args.download_new:
        io.get_and_save()
    else:
        df = io.load()

        analysis.rank(df)


if __name__ == "__main__":
    args = get_parser().parse_args()

    main(args)
