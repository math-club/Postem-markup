"""Main file."""

__version__ = "Postem 0.1"
__author__ = ["Timéo Arnouts"]

import argparse
import logging
import sys

from src.compiler import parse
from src.logger import file_handler, stream_handler


parser = argparse.ArgumentParser(description="Postem")

parser.add_argument("file",
                    type=str,
                    action="store",
                    help="path of the input file")

parser.add_argument("-t", "--terminal",
                    action="store_true",
                    help="display the output in terminal and exit")

parser.add_argument("-v", "--verbose",
                    action="store_true",
                    help="display logs")  # TODO: write better description.

parser.add_argument("-d", "--debug",
                    action="store_true",
                    help="set debug mode")  # TODO: write better description.

parser.add_argument("-V", "--version",
                    action="store_true",
                    help="print the Postem version number and exit.")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit()
    else:
        input_text = open(args.file, "r").read()

        if args.verbose:
            level = logging.INFO

            if args.debug:
                level = logging.DEBUG

            file_handler.setLevel(level)
            stream_handler.setLevel(level)

        output = parse(input_text, args.verbose)

        if args.terminal:
            print(output)
        else:
            with open(f"{args.file}.out", "w") as f:
                f.write(output)
