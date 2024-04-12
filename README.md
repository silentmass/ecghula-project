# Prepare HULA ECG .txt files for Kubios

Prepare .csv files for Kubios from HULA ECG .txt files.
Fills Nan values with zeros.

Script creates another .csv file with original file name with postfix `_prepared.csv` and a `.log` file

## Installation instructions

1) Download and install Python from <https://www.python.org/downloads/>
2) Open Linux Terminal or Windows PowerShell and check python is installed:
   - `python --version`
3) Download project directory [ecghula-project](https://github.com/silentmass/ecghula-project) from github
   - Click green button __Code__ -> __Download ZIP__ -> __Extract zip to easy location__
4) Go to `ecghula-project` directory in Linux Terminal or `ecghula-project-main` in Windows Command Prompt
5) Skip if in Windows. In Linux Terminal run `chmod +x setup.sh` and then `./setup.sh`
6) Remember to activate environment manually in Windows `venv\Scripts\activate` or in Linux `source ./venv/bin/activate`
7) Skip if in Linux. In windows install package in `ecghula-project-main` with `python -m pip install .`

## Create Windows PowerShell shortcut on desktop

- Right-click on your desktop or in the folder where you want the shortcut.
- Choose New > Shortcut.
- In the location field, enter the path to powershell.exe, followed by -NoExit (to keep the window open after the command runs) and -Command, and then the command to activate your virtual environment.
- Change the project directory accordingly where ecghula-project was installed `change_location`

`C:\Windows\System32\cmd.exe /k "C:\change_location\ecghula-project-main\venv\Scripts\activate.bat"`

## Running script to prepare HULA ECG .txt file

### CASE 1

Example usage in command line (remember to enclose path containing spaces with ""):

`ecghula -i "/Users/juha/Downloads/hula/hula_ecg.txt"`

### CASE 2

You can also pass directory path and iterate through all the directory .txt files

`ecghula -i "/Users/juha/Downloads/hula"`

### CASE 3

If you are in the directory where the .txt file is located you can just run

`ecghula`

## Contact

Used in VTT LaunchPad project MUKAVA

11-04-2024
Juha Leukkunen
<juha.leukkunen@gmail.com>
