@echo off

set temp_file="./_temp.md"
set url=%1

call curl %url%.md > %temp_file%
call md2tex %temp_file%

@REM del %temp_file%