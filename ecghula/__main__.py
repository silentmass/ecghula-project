import sys

from ecghula import util


def main():
    util.print_message(" ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
