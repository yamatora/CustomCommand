@echo off

set dir=%~dp0
set FILE=%1
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
echo ==convert pdf to png

Python %dir%\md2tex\tikz\pdf2png.py %FILE%%ARGS%