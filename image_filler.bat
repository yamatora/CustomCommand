@echo off

set dir=%~dp0
set name=%~1
set ARGS=
setlocal enabledelayedexpansion
set POS=cmd
for %%a in (%*) do (
  if "!pos!"=="cmd" (
    set COMMAND=%%~a
    set POS=arg
  ) else if "!pos!"=="arg" (
    set ARGS=!ARGS! %%a
  )
)

echo ==Fill image

Python %dir%\ImageFiller\image_fill.py %name% %ARGS%