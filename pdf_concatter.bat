@echo off

echo ==Concat pdf files
set FILES=%*

Python C:\Users\yamatora\CustomCommand\PDFConcatter\pdf_concatter.py %FILES%