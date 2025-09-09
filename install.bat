@echo off
echo ================================================
echo Advanced Text Extractor - Installation Script
echo ================================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Python found! Installing required packages...
echo.

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install some packages
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ================================================
echo Installation completed successfully!
echo ================================================
echo.

echo IMPORTANT: You also need to install Tesseract OCR
echo.
echo For Windows:
echo 1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
echo 2. Install it to the default location
echo 3. The script will automatically detect it
echo.

echo Usage Options:
echo.
echo 1. GUI Version (Streamlit):
echo    streamlit run app.py
echo.
echo 2. Command Line Version:
echo    python cli_extractor.py "path/to/your/file.pdf"
echo.
echo 3. Interactive Python:
echo    python text_extractor.py
echo.

pause
