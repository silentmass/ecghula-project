# Prepare HULA .txt files for Kubios

Prepare .csv files for Kubios from HULA ECG .txt files.
Fills Nan values with zeros.

Script creates another .csv file with original file name with postfix `_prepared.csv` and a `.log` file

## Installation instructions

1) Download and install Python from <https://www.python.org/downloads/>
2) Open terminal and type the following to check python is installed:
   - `python --version`
3) Download project directory [ecghula-project](https://github.com/silentmass/ecghula-project) from github
   1) Click green button **Code* -> Download ZIP -> Extract zip to easy location**
4) Go to `ecghula-project` directory in Linux terminal or Windows PowerShell
5) In Windows run `setup.bat` (or in Linux run `chmod +x setup.sh` and then `./setup.sh`)

## Create Windows PowerShell shortcut on desktop

- Right-click on your desktop or in the folder where you want the shortcut.
- Choose New > Shortcut.
- In the location field, enter the path to powershell.exe, followed by -NoExit (to keep the window open after the command runs) and -Command, and then the command to activate your virtual environment.
- Change the project directory accordingly where ecghula-project was installed `change_location`

`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoExit -Command "& {C:\change_location\ecghula-project\venv\Scripts\Activate.ps1}"`

## Running script to prepare HULA ECG .txt file

Example usage in command line (remember to enclose path containing spaces with ""):

`ecghula -d "/Users/juha/Downloads/hula/hula_ecg.txt"`

## Contact

Used in VTT LaunchPad project MUKAVA

11-04-2024
Juha Leukkunen
<juha.leukkunen@gmail.com>