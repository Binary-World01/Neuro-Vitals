@echo off
echo ====================================
echo  Starting Neuro-Vitals Frontend
echo ====================================
echo.
echo Opening frontend in browser...
echo.

cd frontend-app
start http://localhost:5500/integrations.html
python -m http.server 5500
