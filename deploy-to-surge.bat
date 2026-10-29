@echo off
title Deploy TalentAI to Surge
echo ========================================================
echo   Deploying TalentAI to https://talentai-rohan.surge.sh
echo ========================================================
echo.
cd /d "%~dp0"
call npx --yes surge . talentai-rohan.surge.sh
echo.
echo ========================================================
echo   Deployment Process Completed!
echo ========================================================
pause
