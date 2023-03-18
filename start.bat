@echo off
echo %~dp0
set /p "refresh_time=How many times you want to refresh: "

start cmd /k "python %~dp0/scripts/main.py --times=%refresh_time%"