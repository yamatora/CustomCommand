@echo off

echo ==Output .pdf from .md via .tex
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
echo %name%.md -> %name%.pdf

pandoc %name%.md -o %name%.pdf --template=%dir%md2tex\template.tex --pdf-engine=lualatex --pdf-engine-opt=-shell-escape -V documentclass=bxjsarticle -V classoption=pandoc --listings -M classoption=twocolumn %ARGS%

@REM ---
@REM Option
@REM    -N
@REM        章番号
@REM    --toc
@REM        目次
@REM    --trace
@REM        処理内容表示(進捗確認)

@REM ---
@REM documentclass
@REM    - bxjsarticle:  章なしレポート
@REM    - bxjsreport:   章ありレポート
@REM    - bxjsbook:     書籍
@REM    - bxjsslide:    スライド