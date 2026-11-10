@echo off
title TransplantIQ - Competition Demo Launcher
echo ======================================================================
echo    TransplantIQ - Agentic AI Organ Transplant Coordination
echo    Db2Hack 2026 Competition Demo Launcher
echo ======================================================================
echo.

cd /d "%~dp0\.."

echo [1/3] Verifying and Seeding Database...
python scripts\verify_project.py
if errorlevel 1 (
    echo Python not found in path, trying local app data python...
    "%LOCALAPPDATA%\Python\bin\python.exe" scripts\verify_project.py
)

echo.
echo [2/3] Starting FastAPI Backend on port 8000...
where python >nul 2>nul
if %errorlevel% equ 0 (
    start "TransplantIQ Backend" cmd /k "cd backend && set PYTHONPATH=. && python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
) else (
    start "TransplantIQ Backend" cmd /k "cd backend && set PYTHONPATH=. && \"%LOCALAPPDATA%\Python\bin\python.exe\" -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
)

echo.
echo [3/3] Launching Clinical Command Center Frontend in Browser...
timeout /t 2 >nul
start "" "%~dp0..\frontend\index.html"

echo.
echo ======================================================================
echo    TransplantIQ is Running!
echo    - Backend API: http://localhost:8000
echo    - API Docs:    http://localhost:8000/docs
echo    - Frontend:    frontend\index.html
echo ======================================================================
pause

