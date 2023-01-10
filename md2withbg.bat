@echo off

echo ==Output .pdf from .md via .tex
set name=%~n1
set option=%~2
echo %name%.md -> %name%.pdf

pandoc %name%.md -o %name%.pdf --template=C:\Users\ymtr\CustomCommands\md2tex\tpl_background.tex --pdf-engine=lualatex --pdf-engine-opt=-shell-escape -V documentclass=bxjsarticle -V classoption=pandoc --listings -M classoption=twocolumn %option%