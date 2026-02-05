@echo off

echo  ______   __  __  __   __ 
echo ^|    _ ^| ^|  ^|^|  ^|^|  ^| ^|  ^|
echo ^|   ^| ^|^| ^|  ^|^|  ^|^|   ^|_^| ^|
echo ^|   ^|_^|^|_^|  ^|^|  ^|^|       ^|
echo ^|    __  ^|  ^|^|  ^|^|  _    ^|
echo ^|   ^|  ^| ^|  ^|^|  ^|^| ^| ^|   ^|
echo ^|___^|  ^|_^|__^|^|__^|^|_^|  ^|__^|

echo.
echo Starting Application...

start "Backend Server" cmd /k "cd src\backend && .venv\Scripts\activate && python app.py"
start "Frontend Client" cmd /k "cd src\frontend && npm run dev"

echo Servers started.
