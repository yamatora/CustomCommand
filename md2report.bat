@echo off

echo ==Output .pdf from .md via .tex
set name=%~n1
echo "%name%.md -> %name%.pdf"

pandoc %name%.md -o %name%.pdf --template=C:\Users\ymtr\CustomCommand\md2tex\template.tex --pdf-engine=lualatex -N -V documentclass=bxjsreport -V classoption=pandoc