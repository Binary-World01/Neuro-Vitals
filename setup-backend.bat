@echo off
echo ====================================
echo  Neuro-Vitals Backend Setup
echo ====================================
echo.

cd backend

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created. Please edit it with your API keys.
) else (
    echo .env file already exists.
)

echo.
echo ====================================
echo  Setup Complete!
echo ====================================
echo.
echo To start the server:
echo   1. cd backend
echo   2. venv\Scripts\activate
echo   3. python -m app.main
echo.
echo Server will run at: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
pause
