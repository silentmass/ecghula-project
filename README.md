# Prepare HULA .txt files for Kubios

Prepare .csv files for Kubios from HULA ECG .txt files.
Fills Nan values with zeros.

## Contact

Used in VTT LaunchPad project MUKAVA

11-04-2024
Juha Leukkunen
<juha.leukkunen@gmail.com>

## Installation instructions

1) Download and install Python from <https://www.python.org/downloads/>

2) Open terminal and type the following to check python is installed:
   1) `python --version`
3) Download project directory [ecghula-project](https://github.com/silentmass/ecghula-project) from github
4) Go to ecghula-project directory in terminal or command prompt
5) Install package with a command:
   1) `python -m pip install .`

## Prepare HULA ECG .txt file

Example usage in command line (remember add "" if path contains spaces):

`ecghula -d "/Users/juha/Downloads/hula/hula_ecg.txt"`

Script creates another .csv file with original file name
with postfix _prepared.csv and a .log file
