@echo off

echo ==Convert to half page
set name=%~n1
echo "%name%.pdf -> %name%_half.pdf"

Python C:\Users\ymtr\CustomCommand\PDFConverter\pdf_converter.py %name%