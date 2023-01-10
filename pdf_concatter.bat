@echo off

echo ==Concat pdf files
set FILES=%*

Python C:\Users\ymtr\CustomCommand\PDFConcatter\pdf_concatter.py %FILES%