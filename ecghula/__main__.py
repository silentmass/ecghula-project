import sys

from ecghula.util import print_message


def main():
    print_message(" ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
