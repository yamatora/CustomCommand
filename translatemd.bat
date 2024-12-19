@echo off

echo ==Output .md(LaTeX) from .md
set dir=%~dp0
set name=%~n1
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

python %dir%\Translatex\main.py --mkdocs %name%.md%ARGS%

@REM call md2tex.bat tl_%name%.md -N