@echo off
REM Quick start script for demo video
REM Run this to start both MCP server and ngrok

echo ========================================
echo  Mistral Fleet Ops Demo Setup
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run: python -m venv .venv
    echo Then: .venv\Scripts\activate
    echo Then: pip install -e .
    pause
    exit /b 1
)

REM Check if .env exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please create .env with:
    echo   BL_API_KEY=your-key
    echo   BL_WORKSPACE=your-workspace
    pause
    exit /b 1
)

echo [1/4] Testing Qdrant connection...
echo.
.venv\Scripts\python.exe test_qdrant.py
if errorlevel 1 (
    echo.
    echo WARNING: Qdrant test failed!
    echo RAG features may not work, but deployments will still work.
    echo Press any key to continue anyway...
    pause >nul
)

echo.
echo [2/4] Starting MCP Server...
echo.
start "MCP Server" cmd /k "cd /d "%~dp0" && .venv\Scripts\activate && python main.py"

echo Waiting 5 seconds for server to start...
timeout /t 5 /nobreak >nul

echo.
echo [3/4] Starting ngrok tunnel with host header fix...
echo.
start "ngrok Tunnel" cmd /k "ngrok http 8000 --host-header=\"localhost:8000\""

echo.
echo [4/4] Setup Complete!
echo.
echo ========================================
echo  NEXT STEPS:
echo ========================================
echo.
echo 1. Look at the ngrok window for your public URL
echo    (It will look like: https://abc123.ngrok.io)
echo.
echo 2. Copy that URL
echo.
echo 3. Open https://chat.mistral.ai
echo.
echo 4. Go to Settings -^> MCP Servers -^> Add Server
echo.
echo 5. Paste your ngrok URL
echo.
echo 6. Start your demo!
echo.
echo ========================================
echo  DEMO COMMANDS TO TRY:
echo ========================================
echo.
echo "List my available tools"
echo.
echo "Deploy https://github.com/Mistral-MCP-Hackathon-2025/mistral-jump.git to 2 sandboxes"
echo.
echo "Verify all my deployment URLs are live"
echo.
echo ========================================
echo.
echo Press any key to open the demo guide...
pause >nul
start DEMO_VIDEO_SETUP.md
