@echo off
echo ========================================
echo AI Super Studio
echo ========================================
echo.
echo Starting servers...
echo.

start cmd /k "cd backend && venv\Scripts\activate.bat && python app.py"
timeout /t 2 /nobreak > nul

start cmd /k "cd frontend && npm run dev"

echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo Press any key to stop servers...
pause > nul

taskkill /FI "WINDOWTITLE eq *python app.py*" /F
taskkill /FI "WINDOWTITLE eq *npm run dev*" /F
