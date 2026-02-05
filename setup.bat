@echo off

echo  _______  _______  _______  __   __  _______ 
echo ^|       ^|^|       ^|^|       ^|^|  ^| ^|  ^|^|       ^|
echo ^|  _____^|^|    ___^|^|_     _^|^|  ^| ^|  ^|^|    _  ^|
echo ^| ^|_____ ^|   ^|___   ^|   ^|  ^|  ^|_^|  ^|^|   ^|_^| ^|
echo ^|_____  ^|^|    ___^|  ^|   ^|  ^|       ^|^|    ___^|
echo  _____^| ^|^|   ^|___   ^|   ^|  ^|       ^|^|   ^|    
echo ^|_______^|^|_______^|  ^|___^|  ^|_______^|^|___^|    

echo.
echo [SETUP] Initializing Backend Only...
echo.

echo [BACKEND] Setting up Flask...
cd src\backend
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
) else (
    echo Virtual environment exists.
)

call .venv\Scripts\activate
echo Installing dependencies...
pip install -r requirement.txt
deactivate
cd ..\..

echo.
echo Backend setup complete.
echo Note: Frontend setup is skipped. Run "npm install" or "pnpm install" in src/frontend if needed.
pause
