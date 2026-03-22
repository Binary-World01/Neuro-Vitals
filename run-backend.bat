@echo off
echo ====================================
echo  Starting Neuro-Vitals Backend
echo ====================================
echo.

cd backend
call venv\Scripts\activate
python -m app.main
