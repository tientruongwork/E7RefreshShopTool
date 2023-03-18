@ECHO OFF

DEL ".\scripts\coordinates_config.py"


echo Hover to "Refresh" button then hit Enter
pause
python ./scripts/get_pointer_position.py > Output
SET /p REFRESH_BUTTON_RECT=<Output
echo refresh_button_rect = %REFRESH_BUTTON_RECT% > .\scripts\coordinates_config.py
echo Refresh button coordinate captured: %REFRESH_BUTTON_RECT%

echo Click on "Refresh" button, hover to "Confirm" button then hit Enter
pause
python %~dp0/scripts/get_pointer_position.py > Output
SET /p REFRESH_BUTTON_CONFIRM_RECT=<Output
echo refresh_confirm_button_rect = %REFRESH_BUTTON_CONFIRM_RECT% >> .\scripts\coordinates_config.py
echo Refresh button confirm coordinate captured: %REFRESH_BUTTON_CONFIRM_RECT%

echo Click on "Buy" button on any item, hover to "Confirm" button then hit Enter
pause
python %~dp0/scripts/get_pointer_position.py > Output
SET /p BUY_BUTTON_CONFIRM_RECT=<Output
echo buy_confirm_button_rect = %BUY_BUTTON_CONFIRM_RECT% >> .\scripts\coordinates_config.py
echo Buy button confirm coordinate captured: %BUY_BUTTON_CONFIRM_RECT%

echo Hover to the black space between item name and price, then hit Enter
pause
python %~dp0/scripts/get_pointer_position.py > Output
SET /p BLANK_SPACE=<Output
echo blank_rect = %BLANK_SPACE% >> .\scripts\coordinates_config.py
echo Blank space for scrolling coordinate captured: %BLANK_SPACE%

DEL Output