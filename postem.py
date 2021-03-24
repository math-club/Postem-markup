"""Main file."""

__version__ = "Postem 0.1"
__author__ = ["Timéo Arnouts"]

import argparse
import sys


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
                    help="display the output in terminal and exit")

parser.add_argument("-V", "--version",
                    action="store_true",
                    help="Print the Postem version number and exit.")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit()
    elif args.terminal:
        print("Ouput in terminal", args.file)
    else:
        print("Output", args.file)
