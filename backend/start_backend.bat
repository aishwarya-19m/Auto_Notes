@echo off
echo Starting AutoNotes Pro Backend...
echo.

cd /d "%~dp0"
call venv\Scripts\activate.bat

echo Checking if .env file exists...
if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file and add your OpenAI API key!
    echo.
    pause
)

echo Starting backend server...
python main.py

pause

