@echo off
REM Stop all demo processes

echo ========================================
echo  Stopping Demo Processes
echo ========================================
echo.

echo Stopping MCP Server...
taskkill /FI "WindowTitle eq MCP Server*" /T /F 2>nul

echo Stopping ngrok...
taskkill /IM ngrok.exe /F 2>nul

echo.
echo All demo processes stopped!
echo.
pause
