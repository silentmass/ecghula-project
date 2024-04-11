"""Prepare .csv files for Kubios from HULA ECG .txt files.
Fills Nan values with zeros.

Used in VTT LaunchPad project MUKAVA

11-04-2024
Juha Leukkunen
juha.leukkunen@gmail.com

###########

Installation instructions:
1) Download and install Python from https://www.python.org/downloads/

2) Open terminal and type the following to check python is installed:
python --version

2) Download project directory ecghula-project from github

3) Go to ecghula-project directory in terminal

4) Install package with a command:
python -m pip install .

###########

Prepare HULA ECG .txt file

Example usage in command line:
ecghula -d "/Users/juha/Downloads/hula/hula_ecg.txt"

Script creates another .csv file with original file name
with postfix _prepared.csv and a .log file
"""

import click

from ecghula.util import list_directory


@click.command()
@click.option(
    "--dir_path", "-d", default=".", help="HULA ECG file directory or file path"
)
def main(dir_path):
    list_directory(dir_path)


if __name__ == "__main__":
    main()
