@echo off

echo ==Convert to half page
set name=%~n1
echo "%name%.pdf -> %name%_odd.pdf, %name%_even.pdf"

Python C:\Users\ymtr\CustomCommand\PDFSplitter\pdf_splitter.py %name%