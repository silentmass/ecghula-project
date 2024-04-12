r"""Prepare .csv files for Kubios from HULA ECG .txt files.
Fills Nan values with zeros.

Script creates another .csv file with original file name
with postfix `_prepared.csv` and a `.log` file

Used in VTT LaunchPad project MUKAVA

11-04-2024
Juha Leukkunen
juha.leukkunen@gmail.com

###########

Installation instructions:
1) Download and install Python from https://www.python.org/downloads/

2) Open terminal and type the following to check python is installed:
python --version

2) Download project directory ecghula-project from
github https://github.com/silentmass/ecghula-project

3) Go to ecghula-project directory in terminal

4) In Windows double click `setup.bat` or
run in PowerShell `.\setup.bat`
(or in Linux Terminal run `chmod +x setup.sh` and then `./setup.sh`)
5) Finally, remember to activate environment manually
in Windows `venv\Scripts\activate` or
in Linux `source ./venv/bin/activate`

###########

Prepare HULA ECG .txt file

Example usage in command line
(remember to enclose path containing spaces with ""):

CASE 1:

`ecghula -i "/Users/juha/Downloads/hula/hula_ecg.txt"`

CASE 2:

You can also pass directory path and
iterate through all the directory .txt files

`ecghula -i "/Users/juha/Downloads/hula"`

CASE 3:

If you are in the directory where the .txt file is located you can just run

`ecghula`
"""

import click

from ecghula.util import list_directory


@click.command()
@click.option("--input_path", "-i", default=".",
              help="HULA ECG directory or file path.")
def main(input_path):
    list_directory(input_path)


if __name__ == "__main__":
    main()
