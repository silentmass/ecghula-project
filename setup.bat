@echo off
REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    exit /b 1
)

REM Optional: Create and activate a virtual environment
echo Creating and activating a virtual environment...
python -m venv venv
venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to create or activate the virtual environment.
    exit /b 1
)

REM Install the package, including any build dependencies as specified in pyproject.toml
echo Installing the package...
python -m pip install .
if %errorlevel% neq 0 (
    echo Failed to install the package.
    exit /b 1
)

echo Setup complete.
