@echo off
title Reset / Logout Surge Account
echo ========================================================
echo   Logging out from current Surge account...
echo ========================================================
echo.
cd /d "%~dp0"
call npx --yes surge logout
echo.
echo ========================================================
echo   Logged out successfully!
echo   Ab aap deploy-to-surge.bat chalayein aur sahi email dalein.
echo ========================================================
pause
